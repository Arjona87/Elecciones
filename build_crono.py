"""Anexa la hoja CRONOGRAMA al libro de auditoria, con vista Gantt por semana."""
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

RUTA = "/mnt/user-data/outputs/AUDITORIA_4MUNICIPIOS.xlsx"
wb = load_workbook(RUTA)
if "CRONOGRAMA" in wb.sheetnames:
    del wb["CRONOGRAMA"]
ws = wb.create_sheet("CRONOGRAMA", 0)

AZUL = "18345D"; NAR = "F08013"
F_HDR = Font(name="Arial", bold=True, size=10, color="FFFFFF")
F_B = Font(name="Arial", size=10)
F_BB = Font(name="Arial", size=10, bold=True)
FILL_HDR = PatternFill("solid", fgColor=AZUL)
FILL_DONE = PatternFill("solid", fgColor="4C7A34")   # ejecutado
FILL_GO = PatternFill("solid", fgColor="F08013")     # en curso / programado
FILL_DEP = PatternFill("solid", fgColor="BDD7EE")    # dependiente de insumo externo
FILL_HITO = PatternFill("solid", fgColor="C00000")   # hito
THIN = Border(*[Side(style="thin", color="D9D9D9")] * 4)

# Semanas: S1 arranca el lunes siguiente al corte de trabajo
SEM = [f"S{i}" for i in range(1, 15)]

COLS = ["#", "Fase", "Entregable", "Responsable", "Depende de", "Estado", "Criterio de cierre"]
W = [4, 26, 40, 14, 16, 13, 46]

TAREAS = [
 # (#, fase, entregable, resp, depende, estado, criterio, semana_ini, semana_fin, tipo)
 (1, "Fase 0 · Extracción", "Guadalajara y Zapopan (22 láminas)", "CGES/DGAPP", "—",
  "Concluido", "Cierre al 100 % en las 26 olas; error de calibración ≤0.26 pp", 1, 1, "done"),
 (2, "Fase 0 · Extracción", "Tlajomulco y Tlaquepaque (26 láminas)", "CGES/DGAPP", "T1",
  "Concluido", "Cierre al 100 % en las 28 olas; error ≤0.15 pp", 1, 2, "done"),
 (3, "Fase 0 · Extracción", "Tonalá y El Salto (20 láminas)", "CGES/DGAPP", "T2",
  "Concluido", "Cierre al 100 % en sus 26 olas", 2, 2, "done"),
 (4, "Fase 0 · Extracción", "Puerto Vallarta (12 láminas)", "CGES/DGAPP", "T3",
  "Concluido", "Cierre al 100 % en sus 13 olas; serie arranca en ago-25", 2, 2, "done"),
 (5, "Fase 0 · Extracción", "Resolución de las 92 celdas ocluidas restantes", "CGES/DGAPP", "T4",
  "Programado", "≤2 % de celdas AUSENTES sobre el registro total (hoy 4.1 %)", 3, 4, "go"),
 (6, "Fase 1 · Auditoría", "Cierre de la hoja AUDITORÍA y PENDIENTES", "CGES/DGAPP", "T5",
  "Programado", "Cada hallazgo con diagnóstico y resolución trazable a página", 4, 4, "go"),
 (7, "Fase 1 · Auditoría", "Validación cruzada por segundo revisor", "CGES/DGAPP", "T6",
  "Programado", "Muestra del 10 % releída a ciegas; discrepancia <0.5 pp", 4, 5, "go"),
 (8, "Fase 2 · Datos", "Esquema definitivo con olas heterogéneas", "CGES/DGAPP", "T5",
  "Programado", "Soporta series de 3 a 14 olas sin matriz fija", 4, 5, "go"),
 (9, "Fase 2 · Datos", "Script de ingesta de olas nuevas", "CGES/DGAPP", "T8",
  "Programado", "Añadir una ola no requiere tocar código del dashboard", 5, 6, "go"),
 (10, "Fase 2 · Datos", "Libro Excel de los 7 municipios", "CGES/DGAPP", "T8",
  "Programado", "Recálculo sin errores de fórmula; suma de control en verde", 5, 6, "go"),
 (11, "Fase 3 · Dashboard", "Escalado del tablero a 7 municipios", "CGES/DGAPP", "T10",
  "Programado", "Carga <2 s con la serie completa; drill-down en URL", 6, 7, "go"),
 (12, "Fase 3 · Dashboard", "Banco de 20+ gráficas con justificación", "CGES/DGAPP", "T11",
  "Programado", "Cada gráfica con título afirmativo y uso para decidir", 7, 8, "go"),
 (13, "Fase 3 · Dashboard", "Mapa Leaflet con GeoJSON municipal", "CGES/DGAPP", "T11",
  "Programado", "118 municipios sin medición en gris; sin imputación espacial", 7, 9, "go"),
 (14, "Fase 3 · Dashboard", "Exportación PNG y CSV por vista", "CGES/DGAPP", "T12",
  "Programado", "Exporta la vista filtrada, no el total", 9, 9, "go"),
 (15, "Fase 4 · Método", "Notas metodológicas completas", "CGES/DGAPP", "T7",
  "Programado", "Margen de la diferencia, universos U1/U2 y límites del método IVR", 6, 7, "go"),
 (16, "Fase 4 · Método", "Dictamen sobre el margen de error declarado", "CGES/DGAPP", "T15",
  "Programado", "Hipótesis del efecto de diseño documentada, sin corregir la fuente", 7, 8, "go"),
 (17, "Fase 4 · Método", "Protocolo de ruptura de serie", "CGES/DGAPP", "T15",
  "Programado", "Regla escrita para cuando cambie la casa encuestadora", 8, 8, "go"),
 (18, "Fase 5 · Gobierno", "Dictamen de derechos y veda electoral", "Jurídico",
  "T15", "Requiere externo", "Criterio escrito sobre difusión en veda", 6, 8, "dep"),
 (19, "Fase 5 · Gobierno", "Decisión de arquitectura de publicación", "Dirección", "T11",
  "Requiere externo", "Hosting y control de acceso definidos por la Dirección", 8, 9, "dep"),
 (20, "Fase 5 · Gobierno", "Definición del logotipo del cliente", "Dirección", "—",
  "Requiere externo", "Sustituye el marcador [LOGO_CLIENTE_PLACEHOLDER]", 9, 9, "dep"),
 (21, "Fase 6 · Entrega", "Pruebas de aceptación y corrección", "CGES/DGAPP", "T14",
  "Programado", "Recorrido de la lista de verificación sin incidencias abiertas", 10, 11, "go"),
 (22, "Fase 6 · Entrega", "Sesión de entrega y capacitación de uso", "CGES/DGAPP", "T21",
  "Programado", "Usuario ejecuta drill-down y exportación sin asistencia", 11, 11, "go"),
 (23, "Fase 7 · Operación", "Ingesta de la ola de septiembre 2026", "CGES/DGAPP", "T9",
  "Depende de fuente", "Publicación de Massive Caller; ingesta en ≤48 h", 8, 8, "dep"),
 (24, "Fase 7 · Operación", "Ingesta de la ola de octubre 2026", "CGES/DGAPP", "T23",
  "Depende de fuente", "Ingesta en ≤48 h y validación de cierre al 100 %", 12, 12, "dep"),
 (25, "Fase 7 · Operación", "Informe ejecutivo mensual de movimientos", "CGES/DGAPP", "T24",
  "Programado", "Una página con lo que cambió por encima del margen de error", 13, 14, "go"),
]

HITOS = [
 ("Registro de los 7 municipios cerrado y auditado", 5),
 ("Dashboard y libro completos en versión candidata", 9),
 ("Entrega formal al cliente", 11),
 ("Primer ciclo mensual operando en régimen", 14),
]

# encabezado
for i, (c, w) in enumerate(zip(COLS, W), 1):
    cell = ws.cell(2, i, c)
    cell.font = F_HDR; cell.fill = FILL_HDR
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.column_dimensions[get_column_letter(i)].width = w
for j, s in enumerate(SEM, len(COLS) + 1):
    cell = ws.cell(2, j, s)
    cell.font = F_HDR; cell.fill = FILL_HDR
    cell.alignment = Alignment(horizontal="center")
    ws.column_dimensions[get_column_letter(j)].width = 4.4

t = ws.cell(1, 1, "Cronograma del proyecto — Preferencia electoral municipal, Jalisco 2027")
t.font = Font(name="Poppins", bold=True, size=13, color=AZUL)
ws.row_dimensions[2].height = 28

FILLS = {"done": FILL_DONE, "go": FILL_GO, "dep": FILL_DEP}
r = 3
for (n, fase, ent, resp, dep, est, crit, s0, s1, tipo) in TAREAS:
    for i, v in enumerate([n, fase, ent, resp, dep, est, crit], 1):
        c = ws.cell(r, i, v); c.font = F_B; c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 6).font = F_BB
    for k in range(s0, s1 + 1):
        cel = ws.cell(r, len(COLS) + k)
        cel.fill = FILLS[tipo]; cel.border = THIN
    ws.row_dimensions[r].height = 26
    r += 1

r += 1
ws.cell(r, 2, "HITOS").font = F_BB
for nombre, sem in HITOS:
    r += 1
    ws.cell(r, 3, nombre).font = F_BB
    cel = ws.cell(r, len(COLS) + sem, "◆")
    cel.fill = FILL_HITO
    cel.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cel.alignment = Alignment(horizontal="center")

r += 2
ws.cell(r, 2, "LEYENDA").font = F_BB
leyenda = [("Verde", "Ejecutado y verificado", FILL_DONE),
           ("Naranja", "Programado, depende solo del equipo", FILL_GO),
           ("Azul", "Requiere insumo o decisión externa al equipo", FILL_DEP),
           ("Rojo ◆", "Hito de control", FILL_HITO)]
for nom, desc, fill in leyenda:
    r += 1
    c = ws.cell(r, 2, nom); c.fill = fill; c.font = F_BB
    ws.cell(r, 3, desc).font = F_B

r += 2
notas = [
 "Las semanas son relativas al arranque; no se fijan fechas de calendario porque tres tareas "
 "dependen de decisiones externas (T18, T19, T20) y una del calendario de publicación de la fuente.",
 "La ruta crítica es T3 → T4 → T5 → T6 → T8 → T10 → T11 → T12 → T14 → T21 → T22. Un retraso ahí "
 "empuja la entrega; los demás bloques tienen holgura.",
 "El riesgo principal previsto era T5 (celdas ocluidas). Ejecutada la extracción completa, la "
 "densidad de solapamiento resultó menor a la temida: quedan 92 celdas, concentradas en las "
 "internas de MORENA, donde hasta 6 precandidatos comparten un mismo tono de rojo.",
 "T23 y T24 son de operación, no de construcción: validan que el sistema absorbe una ola nueva "
 "sin intervención de código. Si esa prueba falla, se reabre T9.",
]
ws.cell(r, 2, "NOTAS").font = F_BB
for n in notas:
    r += 1
    c = ws.cell(r, 3, n); c.font = Font(name="Arial", size=9)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
    ws.row_dimensions[r].height = 30

ws.freeze_panes = "H3"
wb.save(RUTA)
print("hoja CRONOGRAMA añadida;", len(TAREAS), "tareas,", len(HITOS), "hitos")
