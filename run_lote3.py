"""Fase 0 - lote 3: Puerto Vallarta, El Salto y Tonala."""
import json
import extractor3 as E
from extractor3 import run

_o = E.clusters
E.clusters = lambda m, x, halfwin=2, gap=3, min_px=6, _f=_o: _f(m, x, halfwin, gap, min_px)
BOX = (255, 650, 110, 1050)

TODAS = ["2025-07-12", "2025-08-12", "2025-09-12", "2025-10-12", "2025-11-12", "2025-12-12",
         "2026-01-12", "2026-02-12", "2026-03-12", "2026-04-12", "2026-05-12", "2026-06-12",
         "2026-07-12", "2026-08-12"]
F13 = TODAS[1:]          # ago-25 .. ago-26
F10 = TODAS[4:]          # nov-25 .. ago-26
F07 = TODAS[7:]          # feb-26 .. ago-26
F06 = TODAS[8:]          # mar-26 .. ago-26
F05 = TODAS[9:]          # abr-26 .. ago-26
F04 = TODAS[10:]         # may-26 .. ago-26

AZ = (25, 32, 90); GR = (115, 115, 115); NE = (0, 0, 0)
RM = (185, 0, 0); RP = (245, 5, 5); NA = (210, 117, 5)
AM = (224, 210, 0); VE = (0, 170, 85)
PV = "Puerto Vallarta"; ES = "El Salto"; TO = "Tonalá"

LAM = {
 # ---------------- Puerto Vallarta ----------------
 15: dict(muni=PV, tipo="INTENCION_PARTIDO", partido=None, fechas=F13, x=(126, 1010), series=[
   dict(name="MORENA", rgb=RM, final=34.7), dict(name="AÚN NO DECIDE", rgb=NE, final=19.0),
   dict(name="MC", rgb=NA, final=13.3), dict(name="PAN", rgb=AZ, final=12.3),
   dict(name="PRI", rgb=RP, final=11.7), dict(name="PT", rgb=AM, final=5.3),
   dict(name="PVEM", rgb=VE, final=3.7)]),
 17: dict(muni=PV, tipo="PRECANDIDATO", partido="PAN", fechas=F06, x=(167, 968), series=[
   dict(name="JUAN IGNACIO CALDERÓN IBARRÍA", rgb=AZ, final=43.7),
   dict(name="AÚN NO DECIDE", rgb=NE, final=21.8),
   dict(name="OTRO", rgb=GR, final=19.2),
   dict(name="ARNULFO ORTEGA CONTRERAS (DON CHONITO)", rgb=AZ, final=15.3)]),
 19: dict(muni=PV, tipo="PRECANDIDATO", partido="MORENA", fechas=F07, x=(157, 980), series=[
   dict(name="RA AGUILAR ESTRADA", rgb=RM, final=27.5),
   dict(name="OTRO", rgb=GR, final=25.3),
   dict(name="AÚN NO DECIDE", rgb=NE, final=15.5),
   dict(name="FLOR ELIZABETH MICHEL LÓPEZ", rgb=RM, final=11.5),
   dict(name="BRUNO BLANCAS MERCADO", rgb=RM, final=10.9),
   dict(name="SARA MOSQUEDA TORRES", rgb=RM, final=9.3)]),
 21: dict(muni=PV, tipo="PRECANDIDATO", partido="MC", fechas=F07, x=(157, 980), series=[
   dict(name="OTRO", rgb=GR, final=28.4),
   dict(name="DIEGO FRANCO JIMÉNEZ", rgb=NA, final=27.2),
   dict(name="RAMÓN GUERRERO MARTÍNEZ", rgb=NA, final=25.9),
   dict(name="AÚN NO DECIDE", rgb=NE, final=18.5)]),
 23: dict(muni=PV, tipo="PRECANDIDATO", partido="PVEM", fechas=F07, x=(157, 980), series=[
   dict(name="LUIS ERNESTO MUNGUÍA GONZÁLEZ", rgb=VE, final=63.3),
   dict(name="AÚN NO DECIDE", rgb=NE, final=16.7),
   dict(name="OTRO", rgb=GR, final=15.6),
   dict(name="MELISSA MADERO PLASCENCIA", rgb=VE, final=4.4)]),
 25: dict(muni=PV, tipo="REELECCION", partido="PVEM", fechas=F13, x=(126, 1010), series=[
   dict(name="NO", rgb=(200, 20, 20), final=84.4),
   dict(name="SÍ", rgb=(0, 15, 70), final=15.6)]),

 # ---------------- El Salto ----------------
 27: dict(muni=ES, tipo="INTENCION_PARTIDO", partido=None, fechas=F13, x=(125, 1010), series=[
   dict(name="MORENA", rgb=RM, final=39.2), dict(name="MC", rgb=NA, final=16.9),
   dict(name="AÚN NO DECIDE", rgb=NE, final=16.3), dict(name="PRI", rgb=RP, final=10.3),
   dict(name="PAN", rgb=AZ, final=8.3), dict(name="PT", rgb=AM, final=5.3),
   dict(name="PVEM", rgb=VE, final=3.7)]),
 29: dict(muni=ES, tipo="PRECANDIDATO", partido="PAN", fechas=F06, x=(168, 968), series=[
   dict(name="OTRO", rgb=GR, final=30.2),
   dict(name="ADRIÁN FLORES VÉLEZ", rgb=AZ, final=27.1),
   dict(name="AÚN NO DECIDE", rgb=NE, final=22.1),
   dict(name="EFRÉN MENDOZA CARRILLO", rgb=AZ, final=20.6)]),
 31: dict(muni=ES, tipo="PRECANDIDATO", partido="PRI", fechas=F04, x=(207, 929), series=[
   dict(name="NALLELY RAQUEL GONZÁLEZ ÁLVAREZ", rgb=RP, final=36.8),
   dict(name="JOEL GONZÁLEZ DÍAZ", rgb=RP, final=26.3),
   dict(name="OTRO", rgb=GR, final=21.1),
   dict(name="AÚN NO DECIDE", rgb=NE, final=15.8)]),
 33: dict(muni=ES, tipo="PRECANDIDATO", partido="MORENA", fechas=F05, x=(183, 949), series=[
   dict(name="MARÍA ELENA \"NENA\" FARÍAS VILLAFÁN", rgb=RM, final=37.6),
   dict(name="OTRO", rgb=GR, final=24.7),
   dict(name="AÚN NO DECIDE", rgb=NE, final=17.8),
   dict(name="ADRIÁN VENEGAS BERMÚDEZ", rgb=RM, final=13.4),
   dict(name="GABRIEL PÉREZ PÉREZ", rgb=RM, final=6.5)]),
 35: dict(muni=ES, tipo="PRECANDIDATO", partido="MC", fechas=F04, x=(207, 930), series=[
   dict(name="AÚN NO DECIDE", rgb=NE, final=29.8),
   dict(name="OTRO", rgb=GR, final=26.1),
   dict(name="ESTEFANÍA PADILLA MARTÍNEZ", rgb=NA, final=17.1),
   dict(name="RICARDO ZAID SANTILLÁN", rgb=NA, final=14.4),
   dict(name="JORGE ANTONIO VIDALES VARGAS", rgb=NA, final=12.6)]),
 37: dict(muni=ES, tipo="REELECCION", partido="MORENA", fechas=F10, x=(135, 1000), series=[
   dict(name="NO", rgb=(200, 20, 20), final=56.9),
   dict(name="SÍ", rgb=(0, 15, 70), final=43.1)]),

 # ---------------- Tonalá ----------------
 65: dict(muni=TO, tipo="INTENCION_PARTIDO", partido=None, fechas=F13, x=(127, 1010), series=[
   dict(name="MORENA", rgb=RM, final=41.8), dict(name="AÚN NO DECIDE", rgb=NE, final=14.8),
   dict(name="MC", rgb=NA, final=13.4), dict(name="PRI", rgb=RP, final=12.7),
   dict(name="PAN", rgb=AZ, final=11.4), dict(name="PT", rgb=AM, final=3.6),
   dict(name="PVEM", rgb=VE, final=2.3)]),
 67: dict(muni=TO, tipo="PRECANDIDATO", partido="PAN", fechas=F07, x=(156, 979), series=[
   dict(name="OTRO", rgb=GR, final=36.3),
   dict(name="ROCÍO ACOSTA", rgb=AZ, final=33.9),
   dict(name="AÚN NO DECIDE", rgb=NE, final=29.8)]),
 69: dict(muni=TO, tipo="PRECANDIDATO", partido="MORENA", fechas=F07, x=(156, 980), series=[
   dict(name="OTRO", rgb=GR, final=20.6),
   dict(name="LAURA PLASCENCIA PACHECO", rgb=RM, final=20.2),
   dict(name="LILIANA OLÉA FRÍAS", rgb=RM, final=19.2),
   dict(name="EDGAR OSWALDO BAÑALES OROZCO", rgb=RM, final=15.4),
   dict(name="MARTHA ESTELA ARIZMENDI FOMBONA", rgb=RM, final=13.5),
   dict(name="AÚN NO DECIDE", rgb=NE, final=11.1)]),
 71: dict(muni=TO, tipo="PRECANDIDATO", partido="MC", fechas=F07, x=(155, 981), series=[
   dict(name="OTRO", rgb=GR, final=38.3),
   dict(name="JORGE VIZCARRA MAYORGA", rgb=NA, final=31.3),
   dict(name="AÚN NO DECIDE", rgb=NE, final=24.1),
   dict(name="MARY \"CHUY\" REYNOSO TOSTADO", rgb=NA, final=6.3)]),
}

BARRAS = {
 14: (PV, "INTENCION_PARTIDO", None, [("MORENA", 34.7), ("MC", 13.3), ("PAN", 12.3),
      ("PRI", 11.7), ("PT", 5.3), ("PVEM", 3.7), ("AÚN NO DECIDE", 19.0)]),
 16: (PV, "PRECANDIDATO", "PAN", [("JUAN IGNACIO CALDERÓN IBARRÍA", 43.7),
      ("ARNULFO ORTEGA CONTRERAS (DON CHONITO)", 15.3), ("OTRO", 19.2),
      ("AÚN NO DECIDE", 21.8)]),
 18: (PV, "PRECANDIDATO", "MORENA", [("RA AGUILAR ESTRADA", 27.5),
      ("FLOR ELIZABETH MICHEL LÓPEZ", 11.5), ("BRUNO BLANCAS MERCADO", 10.9),
      ("SARA MOSQUEDA TORRES", 9.3), ("OTRO", 25.3), ("AÚN NO DECIDE", 15.5)]),
 20: (PV, "PRECANDIDATO", "MC", [("DIEGO FRANCO JIMÉNEZ", 27.2),
      ("RAMÓN GUERRERO MARTÍNEZ", 25.9), ("OTRO", 28.4), ("AÚN NO DECIDE", 18.5)]),
 22: (PV, "PRECANDIDATO", "PVEM", [("LUIS ERNESTO MUNGUÍA GONZÁLEZ", 63.3),
      ("MELISSA MADERO PLASCENCIA", 4.4), ("OTRO", 15.6), ("AÚN NO DECIDE", 16.7)]),
 24: (PV, "REELECCION", "PVEM", [("SÍ", 15.6), ("NO", 84.4)]),
 26: (ES, "INTENCION_PARTIDO", None, [("MORENA", 39.2), ("MC", 16.9), ("PRI", 10.3),
      ("PAN", 8.3), ("PT", 5.3), ("PVEM", 3.7), ("AÚN NO DECIDE", 16.3)]),
 28: (ES, "PRECANDIDATO", "PAN", [("ADRIÁN FLORES VÉLEZ", 27.1),
      ("EFRÉN MENDOZA CARRILLO", 20.6), ("OTRO", 30.2), ("AÚN NO DECIDE", 22.1)]),
 30: (ES, "PRECANDIDATO", "PRI", [("NALLELY RAQUEL GONZÁLEZ ÁLVAREZ", 36.8),
      ("JOEL GONZÁLEZ DÍAZ", 26.3), ("OTRO", 21.1), ("AÚN NO DECIDE", 15.8)]),
 32: (ES, "PRECANDIDATO", "MORENA", [("MARÍA ELENA \"NENA\" FARÍAS VILLAFÁN", 37.6),
      ("ADRIÁN VENEGAS BERMÚDEZ", 13.4), ("GABRIEL PÉREZ PÉREZ", 6.5), ("OTRO", 24.7),
      ("AÚN NO DECIDE", 17.8)]),
 34: (ES, "PRECANDIDATO", "MC", [("ESTEFANÍA PADILLA MARTÍNEZ", 17.1),
      ("RICARDO ZAID SANTILLÁN", 14.4), ("JORGE ANTONIO VIDALES VARGAS", 12.6),
      ("OTRO", 26.1), ("AÚN NO DECIDE", 29.8)]),
 36: (ES, "REELECCION", "MORENA", [("SÍ", 43.1), ("NO", 56.9)]),
 64: (TO, "INTENCION_PARTIDO", None, [("MORENA", 41.8), ("MC", 13.4), ("PRI", 12.7),
      ("PAN", 11.4), ("PT", 3.6), ("PVEM", 2.3), ("AÚN NO DECIDE", 14.8)]),
 66: (TO, "PRECANDIDATO", "PAN", [("ROCÍO ACOSTA", 33.9), ("OTRO", 36.3),
      ("AÚN NO DECIDE", 29.8)]),
 68: (TO, "PRECANDIDATO", "MORENA", [("LAURA PLASCENCIA PACHECO", 20.2),
      ("LILIANA OLÉA FRÍAS", 19.2), ("EDGAR OSWALDO BAÑALES OROZCO", 15.4),
      ("MARTHA ESTELA ARIZMENDI FOMBONA", 13.5), ("OTRO", 20.6), ("AÚN NO DECIDE", 11.1)]),
 70: (TO, "PRECANDIDATO", "MC", [("JORGE VIZCARRA MAYORGA", 31.3),
      ("MARY \"CHUY\" REYNOSO TOSTADO", 6.3), ("OTRO", 38.3), ("AÚN NO DECIDE", 24.1)]),
}

OVERRIDE = {
 19: {"RA AGUILAR ESTRADA": 343.8, "OTRO": 367.5, "AÚN NO DECIDE": 473.5,
      "FLOR ELIZABETH MICHEL LÓPEZ": 517.0, "BRUNO BLANCAS MERCADO": 523.5,
      "SARA MOSQUEDA TORRES": 542.0},
}
MANUAL = {
 (27, "PVEM", "2025-08-12"): (2.9, "Marcador superpuesto exactamente con PT; lectura por ampliación (y=620)"),
 (27, "PRI", "2026-05-12"): (13.5, "Marcador oculto tras AÚN NO DECIDE en el cruce; lectura por ampliación (y=539)"),
 (27, "PVEM", "2026-05-12"): (2.6, "Marcador superpuesto con PT; lectura por ampliación (y=622)"),
}


def cerrar_por_residual(obs):
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
                if (s["name"], i) in solap and v is not None:
                    nota = "Serie superpuesta con otra del mismo color en esta ola"
                if (pg, s["name"], fecha) in MANUAL:
                    v, nota = MANUAL[(pg, s["name"], fecha)]
                    est = "PONDERADO"
                if v is None:
                    est, nota = "AUSENTE", "Marcador ocluido; no resuelto automáticamente"
                obs.append(dict(ola=fecha, municipio=cf["muni"], tipo_pregunta=cf["tipo"],
                                partido_contexto=cf["partido"], actor=s["name"],
                                valor_pct=v, pagina=pg, estatus=est, nota=nota))
    print("cerradas por residual:", cerrar_por_residual(obs))
    json.dump(dict(observaciones=obs, calibracion=cal),
              open("registro_lote3.json", "w"), ensure_ascii=False, indent=1)
    print("observaciones:", len(obs),
          "| ausentes:", sum(1 for o in obs if o["estatus"] == "AUSENTE"))
    for c in sorted(cal, key=lambda c: -c["error_calibracion_pp"])[:6]:
        print("  pag", c["pagina"], "err", c["error_calibracion_pp"])


if __name__ == "__main__":
    main()
