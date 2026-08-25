"""
Extractor v3 - laminas TRACKING Massive Caller.

Resuelve el caso dificil: varias series comparten exactamente el mismo color
(p.ej. 4 precandidatos del PAN en azul marino). Estrategia:

  1. Clasificacion exclusiva de pixel por color.
  2. Por columna (ola) se detectan los clusteres de Y del color.
  3. Las series de ese color se asignan a los clusteres por COSTE MINIMO
     (algoritmo hungaro) contra la posicion de la ola siguiente, recorriendo
     el tiempo hacia atras desde el ancla rotulada.
  4. Calibracion lineal Y->pct por regresion sobre los valores finales.

Toda celda que no se resuelve queda como None y se marca para inspeccion
visual manual; nunca se rellena automaticamente.
"""
import numpy as np
from PIL import Image
from scipy.optimize import linear_sum_assignment

BOX = (255, 675, 110, 1050)


def load(page):
    return np.array(Image.open(f"{page}.jpeg").convert("RGB")).astype(int)


def masks_by_color(a, colors, tol=60, box=BOX):
    y0, y1, x0, x1 = box
    sub = a[y0:y1, x0:x1]
    d = np.stack([np.sqrt(((sub - np.array(c)) ** 2).sum(axis=2)) for c in colors])
    best, dmin = d.argmin(axis=0), d.min(axis=0)
    out = []
    for i in range(len(colors)):
        m = np.zeros(a.shape[:2], bool)
        m[y0:y1, x0:x1] = (best == i) & (dmin < tol)
        out.append(m)
    return out


def clusters(mask, x, halfwin=3, gap=5, min_px=10):
    """Clusteres de Y con filtro de densidad: descarta ecos de antialiasing."""
    xi = int(round(x))
    win = mask[:, max(0, xi - halfwin): xi + halfwin + 1]
    rows = win.sum(axis=1)
    ys = np.where(rows > 0)[0]
    if len(ys) == 0:
        return []
    groups, cur = [], [ys[0]]
    for y in ys[1:]:
        if y - cur[-1] <= gap:
            cur.append(y)
        else:
            groups.append(cur); cur = [y]
    groups.append(cur)
    out = []
    for g in groups:
        if rows[g].sum() >= min_px:                      # densidad suficiente
            out.append(float(np.average(g, weights=rows[g])))
    return out


def run(page, series, n_points, x_first, x_last, tol=60, box=BOX, max_jump_pp=9.0,
        anchor_override=None):
    """
    series: lista de dicts {name, rgb, final, start} donde start = indice de la
            primera ola en que la serie existe (0 = desde el inicio).
    """
    a = load(page)
    colors = sorted({tuple(s["rgb"]) for s in series})
    masks = dict(zip(colors, masks_by_color(a, colors, tol, box)))
    xs = np.linspace(x_first, x_last, n_points)

    # ---- anclas en la ultima ola (seleccion robusta por ajuste global) ----
    cl_by_color = {c: sorted(clusters(masks[c], xs[-1])) for c in colors}
    n_series_color = {c: len([s for s in series if tuple(s["rgb"]) == c]) for c in colors}

    # 1) anclas inequivocas: color con una sola serie y un solo cluster
    anchor = {}
    seed = []
    for s in series:
        c = tuple(s["rgb"])
        if n_series_color[c] == 1 and len(cl_by_color[c]) == 1:
            anchor[s["name"]] = cl_by_color[c][0]
            seed.append((s["final"], cl_by_color[c][0]))

    if len(seed) < 2:   # respaldo: orden por pct dentro de cada color
        for c in colors:
            grp = sorted([s for s in series if tuple(s["rgb"]) == c], key=lambda s: -s["final"])
            for i, s in enumerate(grp):
                if i < len(cl_by_color[c]):
                    anchor[s["name"]] = cl_by_color[c][i]
                    seed.append((s["final"], cl_by_color[c][i]))

    p = np.array([a for a, _ in seed], float); q = np.array([b for _, b in seed], float)
    m0, b0 = np.polyfit(q, p, 1)

    # 2) resto de series: elegir el cluster mas cercano al Y predicho, sin repetir
    for c in colors:
        grp = sorted([s for s in series if tuple(s["rgb"]) == c], key=lambda s: -s["final"])
        libres = [y for y in cl_by_color[c] if y not in [anchor.get(s["name"]) for s in grp]]
        for s in grp:
            if s["name"] in anchor:
                continue
            if not libres:
                anchor[s["name"]] = None
                continue
            y_pred = (s["final"] - b0) / m0
            best = min(libres, key=lambda y: abs(y - y_pred))
            anchor[s["name"]] = best
            libres.remove(best)

    if anchor_override:
        anchor.update(anchor_override)

    pairs = [(s["final"], anchor[s["name"]]) for s in series if anchor.get(s["name"]) is not None]
    pct = np.array([a for a, _ in pairs], float)
    yy = np.array([b for _, b in pairs], float)
    m, b = np.polyfit(yy, pct, 1)
    f = lambda y: m * y + b
    err = float(np.abs(pct - (m * yy + b)).max())

    # salto maximo en pixeles, derivado de la escala real del eje
    max_jump = abs(max_jump_pp / m)

    # ---- trazado hacia atras con asignacion optima por color ----
    ypos = {s["name"]: [None] * n_points for s in series}
    last = {s["name"]: anchor[s["name"]] for s in series}
    for s in series:
        ypos[s["name"]][-1] = anchor[s["name"]]

    for t in range(n_points - 2, -1, -1):
        for c in colors:
            grp = [s for s in series if tuple(s["rgb"]) == c and s.get("start", 0) <= t]
            if not grp:
                continue
            cl = clusters(masks[c], xs[t])
            prev = [last[s["name"]] for s in grp]
            if not cl:
                continue
            cost = np.full((len(grp), len(cl)), 1e6)
            for i, p in enumerate(prev):
                if p is None:
                    continue
                for j, cy in enumerate(cl):
                    if abs(cy - p) <= max_jump:
                        cost[i, j] = abs(cy - p)
            r, cidx = linear_sum_assignment(cost)
            for i, j in zip(r, cidx):
                if cost[i, j] < 1e5:
                    ypos[grp[i]["name"]][t] = cl[j]
                    last[grp[i]["name"]] = cl[j]

    vals = {s["name"]: [None if y is None else round(float(f(y)), 1) for y in ypos[s["name"]]]
            for s in series}
    return vals, err
