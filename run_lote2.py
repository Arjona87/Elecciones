"""Fase 0 - lote 2: Tlajomulco de Zuniga y San Pedro Tlaquepaque."""
import json
import extractor3 as E
from extractor3 import run

_o = E.clusters
E.clusters = lambda m, x, halfwin=2, gap=3, min_px=6, _f=_o: _f(m, x, halfwin, gap, min_px)
BOX = (255, 650, 110, 1050)

F14 = ["2025-07-12", "2025-08-12", "2025-09-12", "2025-10-12", "2025-11-12", "2025-12-12",
       "2026-01-12", "2026-02-12", "2026-03-12", "2026-04-12", "2026-05-12", "2026-06-12",
       "2026-07-12", "2026-08-12"]
F13 = F14[1:]
F12 = F14[2:]
F03 = F14[-3:]

AZUL = (25, 32, 90); GRIS = (115, 115, 115); NEG = (0, 0, 0)
RM = (185, 0, 0); RP = (245, 5, 5); NAR = (210, 117, 5)
AMA = (224, 210, 0); VER = (0, 170, 85)
TLJ = "Tlajomulco de Zúñiga"; TQP = "San Pedro Tlaquepaque"

LAM = {
 39: dict(muni=TLJ, tipo="INTENCION_PARTIDO", partido=None, fechas=F14, x=(123, 1012), series=[
   dict(name="MORENA", rgb=RM, final=35.2), dict(name="MC", rgb=NAR, final=23.9),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=14.2), dict(name="PAN", rgb=AZUL, final=13.3),
   dict(name="PRI", rgb=RP, final=8.6), dict(name="PT", rgb=AMA, final=3.1),
   dict(name="PVEM", rgb=VER, final=1.7)]),
 41: dict(muni=TLJ, tipo="PRECANDIDATO", partido="PAN", fechas=F12, x=(126, 1008), series=[
   dict(name="SALVADOR GÓMEZ", rgb=AZUL, final=28.4),
   dict(name="OTRO", rgb=GRIS, final=26.9),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=24.6),
   dict(name="MARÍA ELENA RIVERA ESTRADA", rgb=AZUL, final=20.1)]),
 43: dict(muni=TLJ, tipo="PRECANDIDATO", partido="PRI", fechas=F12, x=(127, 1009), series=[
   dict(name="MARCOS ROSALÍO TORRES", rgb=RP, final=38.3),
   dict(name="OTRO", rgb=GRIS, final=34.2),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=27.5)]),
 45: dict(muni=TLJ, tipo="PRECANDIDATO", partido="MORENA", fechas=F12, x=(126, 1009), series=[
   dict(name="LOURDES \"LULÚ\" BARRERA RAZO", rgb=RM, final=19.7),
   dict(name="MARCELA MICHEL LÓPEZ", rgb=RM, final=18.3),
   dict(name="TONY ZAPIÉN", rgb=RM, final=15.5),
   dict(name="MARISOL PALACIOS RAMÍREZ", rgb=RM, final=12.7),
   dict(name="ALBERTO MARTÍNEZ GUTIÉRREZ", rgb=RM, final=11.3),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=10.5),
   dict(name="MARIANA CASILLAS GUERRERO", rgb=RM, final=8.5),
   dict(name="OTRO", rgb=GRIS, final=3.5)]),
 47: dict(muni=TLJ, tipo="PRECANDIDATO", partido="MC", fechas=F12, x=(126, 1010), series=[
   dict(name="GERARDO QUIRINO VELÁZQUEZ CHÁVEZ", rgb=NAR, final=62.2),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=12.7),
   dict(name="OTRO", rgb=GRIS, final=11.5),
   dict(name="ADRIANA GABRIELA MEDINA ORTIZ", rgb=NAR, final=9.5),
   dict(name="FABIOLA SERRATOS LÓPEZ", rgb=NAR, final=4.1)]),
 49: dict(muni=TLJ, tipo="REELECCION", partido="MC", fechas=F13, x=(123, 1012), series=[
   dict(name="NO", rgb=(200, 20, 20), final=54.9),
   dict(name="SÍ", rgb=(0, 15, 70), final=45.1)]),

 51: dict(muni=TQP, tipo="INTENCION_PARTIDO", partido=None, fechas=F14, x=(123, 1012), series=[
   dict(name="MORENA", rgb=RM, final=34.8), dict(name="MC", rgb=NAR, final=20.7),
   dict(name="PAN", rgb=AZUL, final=16.3), dict(name="PRI", rgb=RP, final=12.5),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=11.9), dict(name="PT", rgb=AMA, final=2.2),
   dict(name="PVEM", rgb=VER, final=1.6)]),
 53: dict(muni=TQP, tipo="PRECANDIDATO", partido="PAN", fechas=F12, x=(123, 1008), series=[
   dict(name="ISAÍAS CORTÉS BERUMEN", rgb=AZUL, final=25.9),
   dict(name="MARÍA DEL ROSARIO (CHAYITO) VELÁZQUEZ", rgb=AZUL, final=20.4),
   dict(name="MARÍA FERNANDA GONZÁLEZ REYNOSO", rgb=AZUL, final=16.7),
   dict(name="OTRO", rgb=GRIS, final=15.3),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=14.3),
   dict(name="ADENAWER GONZÁLEZ FIERROS", rgb=AZUL, final=7.4)]),
 55: dict(muni=TQP, tipo="PRECANDIDATO", partido="PRI", fechas=F12, x=(126, 1009), series=[
   dict(name="ALFREDO \"EL GÜERO\" BARBA HERNÁNDEZ", rgb=RP, final=33.8),
   dict(name="OTRO", rgb=GRIS, final=24.1),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=21.8),
   dict(name="REGINA MARTÍNEZ GONZÁLEZ", rgb=RP, final=20.3)]),
 57: dict(muni=TQP, tipo="PRECANDIDATO", partido="MORENA", fechas=F12, x=(126, 1009), series=[
   dict(name="LAURA IMELDA PÉREZ SEGURA", rgb=RM, final=40.1),
   dict(name="ALEJANDRA DEL ROCÍO BADILLO LÓPEZ", rgb=RM, final=16.7),
   dict(name="ALBERTO MALDONADO CHAVARÍN", rgb=RM, final=15.6),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=10.4),
   dict(name="JOSÉ LUIS MONTERDE RAMÍREZ", rgb=RM, final=8.9),
   dict(name="OTRO", rgb=GRIS, final=8.3)]),
 59: dict(muni=TQP, tipo="PRECANDIDATO", partido="MC", fechas=F12, x=(126, 1009), series=[
   dict(name="CITLALLI AMAYA", rgb=NAR, final=44.2),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=21.5),
   dict(name="OTRO", rgb=GRIS, final=12.9),
   dict(name="MARCO ANTONIO FUENTES ONTIVEROS", rgb=NAR, final=11.9),
   dict(name="LAURA ALCÁNTAR DÍAZ", rgb=NAR, final=9.5)]),
 61: dict(muni=TQP, tipo="PRECANDIDATO", partido="PVEM", fechas=F03, x=(247, 889), series=[
   dict(name="OTRO", rgb=GRIS, final=39.2),
   dict(name="ALBERTO ALFARO GARCÍA", rgb=VER, final=38.3),
   dict(name="AÚN NO DECIDE", rgb=NEG, final=22.5)]),
 63: dict(muni=TQP, tipo="REELECCION", partido="MORENA", fechas=F12, x=(126, 1009), series=[
   dict(name="NO", rgb=(200, 20, 20), final=59.5),
   dict(name="SÍ", rgb=(0, 15, 70), final=40.5)]),
}

BARRAS = {
 38: (TLJ, "INTENCION_PARTIDO", None, [("MORENA", 35.2), ("MC", 23.9), ("PAN", 13.3),
      ("PRI", 8.6), ("PT", 3.1), ("PVEM", 1.7), ("AÚN NO DECIDE", 14.2)]),
 40: (TLJ, "PRECANDIDATO", "PAN", [("SALVADOR GÓMEZ", 28.4),
      ("MARÍA ELENA RIVERA ESTRADA", 20.1), ("OTRO", 26.9), ("AÚN NO DECIDE", 24.6)]),
 42: (TLJ, "PRECANDIDATO", "PRI", [("MARCOS ROSALÍO TORRES", 38.3), ("OTRO", 34.2),
      ("AÚN NO DECIDE", 27.5)]),
 44: (TLJ, "PRECANDIDATO", "MORENA", [("LOURDES \"LULÚ\" BARRERA RAZO", 19.7),
      ("MARCELA MICHEL LÓPEZ", 18.3), ("TONY ZAPIÉN", 15.5),
      ("MARISOL PALACIOS RAMÍREZ", 12.7), ("ALBERTO MARTÍNEZ GUTIÉRREZ", 11.3),
      ("MARIANA CASILLAS GUERRERO", 8.5), ("OTRO", 3.5), ("AÚN NO DECIDE", 10.5)]),
 46: (TLJ, "PRECANDIDATO", "MC", [("GERARDO QUIRINO VELÁZQUEZ CHÁVEZ", 62.2),
      ("ADRIANA GABRIELA MEDINA ORTIZ", 9.5), ("FABIOLA SERRATOS LÓPEZ", 4.1),
      ("OTRO", 11.5), ("AÚN NO DECIDE", 12.7)]),
 48: (TLJ, "REELECCION", "MC", [("SÍ", 45.1), ("NO", 54.9)]),
 50: (TQP, "INTENCION_PARTIDO", None, [("MORENA", 34.8), ("MC", 20.7), ("PAN", 16.3),
      ("PRI", 12.5), ("PT", 2.2), ("PVEM", 1.6), ("AÚN NO DECIDE", 11.9)]),
 52: (TQP, "PRECANDIDATO", "PAN", [("ISAÍAS CORTÉS BERUMEN", 25.9),
      ("MARÍA DEL ROSARIO (CHAYITO) VELÁZQUEZ", 20.4),
      ("MARÍA FERNANDA GONZÁLEZ REYNOSO", 16.7), ("ADENAWER GONZÁLEZ FIERROS", 7.4),
      ("OTRO", 15.3), ("AÚN NO DECIDE", 14.3)]),
 54: (TQP, "PRECANDIDATO", "PRI", [("ALFREDO \"EL GÜERO\" BARBA HERNÁNDEZ", 33.8),
      ("REGINA MARTÍNEZ GONZÁLEZ", 20.3), ("OTRO", 24.1), ("AÚN NO DECIDE", 21.8)]),
 56: (TQP, "PRECANDIDATO", "MORENA", [("LAURA IMELDA PÉREZ SEGURA", 40.1),
      ("ALEJANDRA DEL ROCÍO BADILLO LÓPEZ", 16.7), ("ALBERTO MALDONADO CHAVARÍN", 15.6),
      ("JOSÉ LUIS MONTERDE RAMÍREZ", 8.9), ("OTRO", 8.3), ("AÚN NO DECIDE", 10.4)]),
 58: (TQP, "PRECANDIDATO", "MC", [("CITLALLI AMAYA", 44.2),
      ("MARCO ANTONIO FUENTES ONTIVEROS", 11.9), ("LAURA ALCÁNTAR DÍAZ", 9.5),
      ("OTRO", 12.9), ("AÚN NO DECIDE", 21.5)]),
 60: (TQP, "PRECANDIDATO", "PVEM", [("ALBERTO ALFARO GARCÍA", 38.3), ("OTRO", 39.2),
      ("AÚN NO DECIDE", 22.5)]),
 62: (TQP, "REELECCION", "MORENA", [("SÍ", 40.5), ("NO", 59.5)]),
}

OVERRIDE = {
 45: {'LOURDES "LULÚ" BARRERA RAZO': 454.3, "MARCELA MICHEL LÓPEZ": 468.3,
      "TONY ZAPIÉN": 494.0, "MARISOL PALACIOS RAMÍREZ": 520.7,
      "ALBERTO MARTÍNEZ GUTIÉRREZ": 533.6, "MARIANA CASILLAS GUERRERO": 560.7},
}
MANUAL = {
 (39, "PAN", "2025-12-12"): (10.1, "Cruce triple con PRI y AÚN NO DECIDE; lectura por ampliación (y=556.7)"),
 (39, "PVEM", "2025-12-12"): (3.0, "Cruce con PT; lectura por ampliación (y=616.7)"),
}


def cerrar_por_residual(obs):
    """Si en una ola de INTENCION_PARTIDO falta EXACTAMENTE una serie y las demas
    suman S, el faltante queda determinado como 100-S. Es aritmetica, no analogia:
    la propia fuente normaliza la pregunta al 100 %. Se marca y se documenta."""
    from collections import defaultdict
    idx = defaultdict(list)
    for o in obs:
        if o["tipo_pregunta"] == "INTENCION_PARTIDO":
            idx[(o["municipio"], o["ola"])].append(o)
    n = 0
    for k, grupo in idx.items():
        faltan = [o for o in grupo if o["valor_pct"] is None]
        if len(faltan) != 1:
            continue
        s = sum(o["valor_pct"] for o in grupo if o["valor_pct"] is not None)
        v = round(100 - s, 1)
        if not (0 <= v <= 100):
            continue
        faltan[0]["valor_pct"] = v
        faltan[0]["estatus"] = "PONDERADO"
        faltan[0]["nota"] = (f"Marcador ocluido. Cerrado por residual: 100 - {s:.1f} = {v}. "
                             "Única serie faltante de la ola.")
        n += 1
    return n


def main():
    obs, cal = [], []
    for pg, (muni, tipo, part, items) in BARRAS.items():
        for actor, pct in items:
            obs.append(dict(ola="2026-08-12", municipio=muni, tipo_pregunta=tipo,
                            partido_contexto=part, actor=actor, valor_pct=pct,
                            pagina=pg, estatus="LITERAL", nota=""))
    for pg, cf in LAM.items():
        vals, err, solap = run(pg, cf["series"], len(cf["fechas"]), cf["x"][0], cf["x"][1],
                        box=BOX, anchor_override=OVERRIDE.get(pg))
        cal.append(dict(pagina=pg, error_calibracion_pp=round(err, 3)))
        for s in cf["series"]:
            for i, fecha in enumerate(cf["fechas"]):
                if i < s.get("start", 0):
                    continue
                v = vals[s["name"]][i]
                if i == len(cf["fechas"]) - 1:
                    est, nota = "LITERAL", ""
                else:
                    est = "PONDERADO"
                    nota = "Serie histórica sin etiqueta numérica en la fuente"
                if (pg, s["name"], fecha) in MANUAL:
                    v, nota = MANUAL[(pg, s["name"], fecha)]
                    est = "PONDERADO"
                if (s["name"], i) in solap and v is not None:
                    nota = "Serie superpuesta con otra del mismo color en esta ola"
                if v is None:
                    est, nota = "AUSENTE", "Marcador ocluido; no resuelto automáticamente"
                obs.append(dict(ola=fecha, municipio=cf["muni"], tipo_pregunta=cf["tipo"],
                                partido_contexto=cf["partido"], actor=s["name"],
                                valor_pct=v, pagina=pg, estatus=est, nota=nota))
    nres = cerrar_por_residual(obs)
    print("cerradas por residual:", nres)
    json.dump(dict(observaciones=obs, calibracion=cal),
              open("registro_lote2.json", "w"), ensure_ascii=False, indent=1)
    print("observaciones:", len(obs),
          "| ausentes:", sum(1 for o in obs if o["estatus"] == "AUSENTE"))
    for c in sorted(cal, key=lambda c: -c["error_calibracion_pp"]):
        print("  pag", c["pagina"], "err", c["error_calibracion_pp"])


if __name__ == "__main__":
    main()
