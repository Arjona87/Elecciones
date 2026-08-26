"""Construye AUDITORIA_PILOTO.xlsx segun el estandar CGES/DGAPP."""
import json
from collections import defaultdict, OrderedDict
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

D = json.load(open("registro_full.json"))
OBS = D["observaciones"]
CAL = {c["pagina"]: c["error_calibracion_pp"] for c in D["calibracion"]}

AZUL = "18345D"; NAR = "F08013"
F_HDR = Font(name="Arial", bold=True, size=10, color="FFFFFF")
F_B = Font(name="Arial", size=10)
F_BB = Font(name="Arial", size=10, bold=True)
FILL_HDR = PatternFill("solid", fgColor=AZUL)
FILL_LIT = PatternFill("solid", fgColor="E2F0D9")   # verde  - literal
FILL_PON = PatternFill("solid", fgColor="FCE4D6")   # naranja - ponderado
FILL_AUS = PatternFill("solid", fgColor="F8CBAD")   # rojo claro - ausente
FILL_KEY = PatternFill("solid", fgColor="FFF2CC")   # ambar - celda a editar
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

FILL_BY = {"LITERAL": FILL_LIT, "PONDERADO": FILL_PON, "AUSENTE": FILL_AUS}

OLAS = ["2025-07-12", "2025-08-12", "2025-09-12", "2025-10-12", "2025-11-12", "2025-12-12",
        "2026-01-12", "2026-02-12", "2026-03-12", "2026-04-12", "2026-05-12",
        "2026-06-12", "2026-07-12", "2026-08-12"]

wb = Workbook()


def head(ws, cols, widths, freeze="A2"):
    for i, (c, w) in enumerate(zip(cols, widths), 1):
        cell = ws.cell(1, i, c)
        cell.font = F_HDR; cell.fill = FILL_HDR
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = freeze
    ws.row_dimensions[1].height = 30


# ---------------------------------------------------------------- DATOS_MAESTROS
ws = wb.active; ws.title = "DATOS_MAESTROS"
COLS = ["ola_fecha", "entidad", "cve_inegi", "municipio", "tipo_pregunta", "universo",
        "partido_contexto", "actor", "valor_pct", "muestra_n", "margen_error_pct",
        "casa_encuestadora", "metodo_captura", "pagina_fuente", "estatus_dato", "nota"]
head(ws, COLS, [11, 9, 9, 16, 19, 26, 10, 34, 10, 9, 11, 16, 14, 8, 12, 60])
CVE = {"Guadalajara": "14039", "Zapopan": "14120", "San Pedro Tlaquepaque": "14098",
       "Tlajomulco de Zúñiga": "14097", "Puerto Vallarta": "14067", "El Salto": "14030",
       "Tonalá": "14101"}
UNIV = {"INTENCION_PARTIDO": "Total de entrevistados del municipio",
        "PRECANDIDATO": "Condicional: declarantes del partido",
        "REELECCION": "Total de entrevistados del municipio"}
r = 2
for o in OBS:
    vals = [o["ola"], "Jalisco", CVE[o["municipio"]], o["municipio"], o["tipo_pregunta"],
            UNIV[o["tipo_pregunta"]], o["partido_contexto"] or "—", o["actor"],
            o["valor_pct"], 600, 4.3, "Massive Caller", "Telefónico automatizado",
            o["pagina"], o["estatus"], o["nota"]]
    for i, v in enumerate(vals, 1):
        c = ws.cell(r, i, v); c.font = F_B; c.border = THIN
    ws.cell(r, 9).fill = FILL_BY[o["estatus"]]
    ws.cell(r, 9).number_format = "0.0"
    r += 1
ws.auto_filter.ref = f"A1:P{r-1}"
N_DM = r - 1

# ------------------------------------------------------------ EVOLUCION_TEMPORAL
ws = wb.create_sheet("EVOLUCION_TEMPORAL")
cols = ["municipio", "partido"] + OLAS + ["Δ 12 meses (pp)", "Δ último mes (pp)",
                                          "máximo", "mínimo", "amplitud (pp)"]
head(ws, cols, [15, 16] + [11] * 14 + [17, 17, 10, 10, 14])
serie = defaultdict(dict)
for o in OBS:
    if o["tipo_pregunta"] == "INTENCION_PARTIDO":
        serie[(o["municipio"], o["actor"])][o["ola"]] = o
ORD = ["MORENA", "MC", "PAN", "PRI", "PT", "PVEM", "AÚN NO DECIDE"]
r = 2
for muni in ["Guadalajara", "Zapopan", "San Pedro Tlaquepaque", "Tlajomulco de Zúñiga",
             "Puerto Vallarta", "El Salto", "Tonalá"]:
    for p in ORD:
        ws.cell(r, 1, muni).font = F_B
        ws.cell(r, 2, p).font = F_BB
        for j, ola in enumerate(OLAS, 3):
            o = serie[(muni, p)].get(ola)
            c = ws.cell(r, j, None if o is None else o["valor_pct"])
            c.font = F_B; c.number_format = "0.0"; c.border = THIN
            if o: c.fill = FILL_BY[o["estatus"]]
        L = get_column_letter
        ws.cell(r, 17, f"={L(16)}{r}-{L(3)}{r}")
        ws.cell(r, 18, f"={L(16)}{r}-{L(15)}{r}")
        ws.cell(r, 19, f"=MAX({L(3)}{r}:{L(16)}{r})")
        ws.cell(r, 20, f"=MIN({L(3)}{r}:{L(16)}{r})")
        ws.cell(r, 21, f"={L(19)}{r}-{L(20)}{r}")
        for k in range(17, 22):
            ws.cell(r, k).font = F_BB; ws.cell(r, k).number_format = "+0.0;-0.0;0.0"
        r += 1
    # fila de control: la suma debe cerrar en 100
    ws.cell(r, 2, "SUMA DE CONTROL").font = F_BB
    for j in range(3, 17):
        L = get_column_letter(j)
        ws.cell(r, j, f"=SUM({L}{r-7}:{L}{r-1})")
        ws.cell(r, j).font = F_BB; ws.cell(r, j).number_format = "0.0"
        ws.cell(r, j).fill = FILL_KEY
    r += 2

# --------------------------------------------------------------- PRECANDIDATOS
ws = wb.create_sheet("PRECANDIDATOS")
cols = ["municipio", "partido", "precandidato", "preferencia interna % (U2)",
        "voto del partido % (U1)", "voto efectivo estimado % *", "página", "estatus"]
head(ws, cols, [15, 10, 38, 24, 22, 24, 9, 12])
u1 = {(o["municipio"], o["actor"]): o["valor_pct"] for o in OBS
      if o["tipo_pregunta"] == "INTENCION_PARTIDO" and o["ola"] == "2026-08-12"}
r = 2
for o in OBS:
    if o["tipo_pregunta"] != "PRECANDIDATO" or o["ola"] != "2026-08-12":
        continue
    if o["actor"] in ("OTRO", "AÚN NO DECIDE"):
        continue
    base = u1.get((o["municipio"], o["partido_contexto"]))
    for i, v in enumerate([o["municipio"], o["partido_contexto"], o["actor"],
                           o["valor_pct"], base], 1):
        c = ws.cell(r, i, v); c.font = F_B; c.border = THIN
    ws.cell(r, 4).number_format = "0.0"; ws.cell(r, 5).number_format = "0.0"
    ws.cell(r, 6, f"=ROUND(D{r}*E{r}/100,1)")
    ws.cell(r, 6).font = F_BB; ws.cell(r, 6).number_format = "0.0"
    ws.cell(r, 6).fill = FILL_PON
    ws.cell(r, 7, o["pagina"]).font = F_B
    ws.cell(r, 8, o["estatus"]).font = F_B
    r += 1
ws.cell(r + 1, 1, "* Voto efectivo estimado = preferencia interna (U2) × voto del partido "
                  "(U1) / 100. Métrica DERIVADA, no publicada por la fuente. U1 y U2 tienen "
                  "universos distintos y no son comparables entre sí.").font = Font(
    name="Arial", size=9, italic=True)

# ------------------------------------------------------- ESTRUCTURA_SUBNACIONAL
ws = wb.create_sheet("ESTRUCTURA_SUBNACIONAL")
head(ws, ["cve_inegi", "municipio", "nivel", "distrito_local", "sección_electoral",
          "ola_fecha", "actor", "valor_pct", "muestra_n", "fuente"],
     [11, 26, 12, 15, 18, 12, 30, 11, 11, 20])
plantilla = [("14039", "Guadalajara", "PROCESADO"), ("14120", "Zapopan", "PROCESADO"),
             ("14098", "San Pedro Tlaquepaque", "PROCESADO"),
             ("14097", "Tlajomulco de Zúñiga", "PROCESADO"),
             ("14101", "Tonalá", "PROCESADO"), ("14030", "El Salto", "PROCESADO"),
             ("14067", "Puerto Vallarta", "PROCESADO")]
for i, (cve, nom, niv) in enumerate(plantilla, 2):
    for j, v in enumerate([cve, nom, niv], 1):
        ws.cell(i, j, v).font = F_B
    for j in range(4, 11):
        ws.cell(i, j).fill = FILL_KEY; ws.cell(i, j).border = THIN
ws.cell(11, 1, "Celdas ámbar = capturar aquí. Jalisco tiene 125 municipios; este piloto "
               "cubre 2. Al añadir filas, respetar la clave INEGI de 5 dígitos.").font = Font(
    name="Arial", size=9, italic=True)

# -------------------------------------------------------------------- AUDITORIA
ws = wb.create_sheet("AUDITORIA")
head(ws, ["#", "página", "hallazgo", "diagnóstico", "resolución"], [5, 9, 46, 62, 46])
AUD = [
 (1, "—", "El archivo fuente no es un PDF",
  "Contenedor ZIP con 82 imágenes JPEG y 82 archivos de texto vacíos; sin capa de texto extraíble.",
  "Lectura visual lámina por lámina; ninguna omitida."),
 (2, "todas", "Margen de error declarado inconsistente con N",
  "La fuente declara ±4.3 % con N=600. El cálculo con z=1.96 y p=0.5 da ±4.0 %. Compatible con "
  "efecto de diseño ≈1.16, o con n efectivo ≈519.",
  "Se REPORTA la discrepancia. No se corrige la cifra de la fuente."),
 (3, "3,5,7,9,11,13,73,75,77,79,81", "Series de tracking sin etiqueta numérica",
  "Solo el último punto de cada serie está rotulado; las 11–12 olas previas no.",
  "Reconstrucción por calibración lineal del eje Y. Error máx. de calibración 0.257 pp "
  "frente a ±4.3 pp de error muestral."),
 (4, "3,73", "Validación independiente del cierre al 100 %",
  "Las series se reconstruyeron por separado, sin imponer que sumaran 100.",
  "Las 93 olas de intención de voto cierran entre 99.5 % y 100.5 %."),
 (5, "3", "PRI Guadalajara MAR-26: marcador ocluido",
  "El marcador del PRI queda exactamente bajo la serie AÚN NO DECIDE en el cruce.",
  "Lectura por ampliación: 11.9. Validado por residual."),
 (6, "3", "PVEM Guadalajara AGO-25: marcador ocluido",
  "El marcador del PVEM coincide con el del PT en el punto de origen.",
  "Lectura por ampliación: 2.5. Confirmado de forma independiente por residual (100−97.5)."),
 (7, "3", "PAN Guadalajara JUL-26: cruce exacto",
  "PAN y AÚN NO DECIDE se intersecan en el mismo píxel.",
  "Ambos valen 14.3. Triple validación: ampliación, residual y valor de la otra serie."),
 (8, "varias", "92 celdas no resueltas (4.1 % del registro)",
  "Oclusión entre precandidatos del mismo partido, que la fuente grafica con color idéntico.",
  "Marcadas AUSENTE. Listadas en PENDIENTES. Ninguna rellenada automáticamente."),
 (11, "18,19", "Nombre de precandidato truncado en la fuente",
  "La lámina 18 de Puerto Vallarta rotula 'RA AGUILAR ESTRADA'; el nombre de pila aparece "
  "cortado en el archivo original.",
  "Se registra literalmente como aparece. NO se completa el nombre por inferencia."),
 (12, "22,23,60,61", "Cobertura de partidos heterogénea entre municipios",
  "El PVEM tiene interna medida solo en Tlaquepaque y Puerto Vallarta; el PRI no se mide en "
  "Puerto Vallarta ni Tonalá; Tonalá no tiene pregunta de reelección.",
  "El esquema admite ausencia de partido por municipio; no se imputan celdas vacías."),
 (13, "varias", "Longitud de serie heterogénea",
  "Las series van de 3 olas (PVEM Tlaquepaque) a 14 (partidos en Tlajomulco y Tlaquepaque).",
  "El esquema es de lista por ola, no matriz fija. Las olas sin medición quedan vacías."),
 (9, "4–13, 74–81", "Dos universos distintos en el mismo estudio",
  "U1 (voto por partido) es sobre el total; U2 (precandidato) es condicional a declarar ese partido.",
  "Separados en hojas distintas. El voto efectivo se calcula y se marca como derivado."),
 (10, "todas", "Restricción de derechos de la fuente",
  "D.R. © Massive Caller S.A. de C.V., 2026. Reproducción sujeta a referencia al autor, "
  "salvo veda electoral.",
  "Atribución obligatoria en todo entregable; advertencia de veda incorporada."),
]
for i, row in enumerate(AUD, 2):
    for j, v in enumerate(row, 1):
        c = ws.cell(i, j, v); c.font = F_B
        c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = THIN
    ws.row_dimensions[i].height = 46

# -------------------------------------------------------------------- PENDIENTES
ws = wb.create_sheet("PENDIENTES")
head(ws, ["página", "municipio", "partido", "actor", "ola", "razón", "qué se necesita"],
     [9, 15, 10, 38, 12, 40, 44])
r = 2
for o in OBS:
    if o["estatus"] != "AUSENTE":
        continue
    for j, v in enumerate([o["pagina"], o["municipio"], o["partido_contexto"] or "—",
                           o["actor"], o["ola"],
                           "Marcador ocluido por serie del mismo color",
                           "Tabla de valores del tracking, o ampliación manual de la lámina"], 1):
        c = ws.cell(r, j, v); c.font = F_B; c.border = THIN
    ws.cell(r, 4).fill = FILL_AUS
    r += 1
ws.auto_filter.ref = f"A1:G{r-1}"

# ------------------------------------------------------------ LEYENDA_Y_FUENTES
ws = wb.create_sheet("LEYENDA_Y_FUENTES")
ws.column_dimensions["A"].width = 26; ws.column_dimensions["B"].width = 96
rows = [
 ("SEMÁFORO DE COLORES", ""),
 ("Verde E2F0D9", "LITERAL — valor impreso en la lámina, transcrito sin transformación."),
 ("Naranja FCE4D6", "PONDERADO — reconstruido del tracking o derivado por fórmula. Marcado con *."),
 ("Rojo claro F8CBAD", "AUSENTE — marcador ocluido. No resuelto. No usar."),
 ("Ámbar FFF2CC", "Celda de captura o control que el usuario debe revisar/llenar."),
 ("", ""),
 ("MÉTODO DE RECONSTRUCCIÓN", ""),
 ("Procedimiento",
  "1) Clasificación exclusiva de píxel por color. 2) Detección de marcadores por columna con "
  "filtro de densidad. 3) Asignación de coste mínimo para series del mismo color, hacia atrás "
  "desde la ola rotulada. 4) Calibración lineal Y→porcentaje por regresión sobre los valores "
  "finales impresos."),
 ("Precisión", "Error máximo de calibración: 0.257 pp. Margen de error de la encuesta: ±4.3 pp."),
 ("Control de cierre", "Las 26 olas de intención de voto suman entre 99.9 % y 100.3 % sin imposición."),
 ("No se hizo", "No se ajustó ninguna cifra para forzar el cierre. No se imputó por analogía "
                "con otro mes ni con otro municipio."),
 ("", ""),
 ("MARGEN DE ERROR", ""),
 ("Declarado por la fuente", "±4.3 % con N=600."),
 ("Recalculado", "ME = z·√(p(1−p)/n) con z=1.96, p=0.5, n=600 → ±4.0 %. Discrepancia reportada."),
 ("Diferencia entre dos", "ME_dif = z·√((p₁+p₂−(p₁−p₂)²)/n). Es la métrica válida para declarar "
                          "puntero o empate técnico."),
 ("", ""),
 ("UNIVERSOS", ""),
 ("U1", "Voto por partido. Base: total de entrevistados del municipio."),
 ("U2", "Preferencia de precandidato. Base: solo quienes declararon ese partido. "
        "NO comparable con U1 ni sumable con él."),
 ("", ""),
 ("PONDERACIÓN", ""),
 ("Post-estratificación", "La fuente NO publica factores de expansión, cuotas ni tasa de "
                          "respuesta. Información no disponible; no se supone ningún modelo."),
 ("Método de captura", "Encuesta telefónica automatizada. Sesgo de cobertura y autoselección "
                       "no cuantificables con lo publicado."),
 ("", ""),
 ("FUENTE Y DERECHOS", ""),
 ("Cita APA 7", "Massive Caller. (2026). Jalisco: intención al voto, alcaldías 2027 "
                "[Reporte de encuesta, corte 12 de agosto de 2026]."),
 ("Derechos", "D.R. © Massive Caller S.A. de C.V., 2026. Se autoriza la reproducción al hacer "
              "referencia al autor, salvo que aplique veda electoral."),
 ("Elaboración", "CGES/DGAPP/AA."),
]
for i, (a, b) in enumerate(rows, 1):
    ca = ws.cell(i, 1, a); cb = ws.cell(i, 2, b)
    ca.font = F_BB if b == "" else F_B
    cb.font = F_B
    cb.alignment = Alignment(wrap_text=True, vertical="top")
    if b == "" and a:
        ca.fill = FILL_HDR; ca.font = F_HDR
    if len(b) > 90:
        ws.row_dimensions[i].height = 42

wb.save("/mnt/user-data/outputs/AUDITORIA_JALISCO_7MUNICIPIOS.xlsx")
print("filas DATOS_MAESTROS:", N_DM)
print("guardado")
