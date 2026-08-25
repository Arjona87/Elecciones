import json
import numpy as np
import extractor3 as E
from extractor3 import run
_o = E.clusters
E.clusters = lambda m, x, halfwin=2, gap=3, min_px=6, _f=_o: _f(m, x, halfwin, gap, min_px)

BOX = (255, 650, 110, 1050)

F13 = ["2025-08-12", "2025-09-12", "2025-10-12", "2025-11-12", "2025-12-12",
       "2026-01-12", "2026-02-12", "2026-03-12", "2026-04-12", "2026-05-12",
       "2026-06-12", "2026-07-12", "2026-08-12"]
F12 = F13[1:]
F07 = F13[6:]

AZUL = (25, 32, 90); GRIS = (115, 115, 115); NEGRO = (0, 0, 0)
ROJO_M = (185, 0, 0); ROJO_P = (245, 5, 5); NAR = (210, 117, 5)
AMA = (224, 210, 0); VER = (0, 170, 85)

LAM = {
 3: dict(muni="Guadalajara", tipo="INTENCION_PARTIDO", partido=None, fechas=F13,
         x=(124, 1010), series=[
   dict(name="MORENA", rgb=ROJO_M, final=32.7), dict(name="MC", rgb=NAR, final=22.1),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=16.4), dict(name="PAN", rgb=AZUL, final=12.9),
   dict(name="PRI", rgb=ROJO_P, final=10.6), dict(name="PT", rgb=AMA, final=3.6),
   dict(name="PVEM", rgb=VER, final=1.7)]),

 5: dict(muni="Guadalajara", tipo="PRECANDIDATO", partido="PAN", fechas=F12,
         x=(128, 1007), series=[
   dict(name="MIGUEL ÁNGEL MONRAZ IBARRA", rgb=AZUL, final=21.4),
   dict(name="OTRO", rgb=GRIS, final=20.2),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=16.7),
   dict(name="DIANA ARACELI GONZÁLEZ MARTÍNEZ", rgb=AZUL, final=16.1),
   dict(name="JOSÉ MIGUEL MENDOZA LARA", rgb=AZUL, final=14.9),
   dict(name="PAOLA ESPINOSA SÁNCHEZ", rgb=AZUL, final=7.1, start=6),
   dict(name="CÉSAR MADRIGAL DÍAZ", rgb=AZUL, final=3.6, start=6)]),

 7: dict(muni="Guadalajara", tipo="PRECANDIDATO", partido="PRI", fechas=F12,
         x=(128, 1007), series=[
   dict(name="LAURA HARO RAMÍREZ", rgb=ROJO_P, final=31.5),
   dict(name="OTRO", rgb=GRIS, final=26.8, start=1),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=17.3),
   dict(name="HORTENSIA NOROÑA QUEZADA", rgb=ROJO_P, final=13.7),
   dict(name="VERÓNICA FLORES PÉREZ", rgb=ROJO_P, final=10.7)]),

 9: dict(muni="Guadalajara", tipo="PRECANDIDATO", partido="MORENA", fechas=F07,
         x=(156, 978), series=[
   dict(name="CARLOS LOMELÍ BOLAÑOS", rgb=ROJO_M, final=35.8),
   dict(name="CHEMA MARTÍNEZ", rgb=ROJO_M, final=16.2),
   dict(name="ITZUL BARRERA RODRÍGUEZ", rgb=ROJO_M, final=14.2),
   dict(name="CARLOS PALACIOS RODRÍGUEZ", rgb=ROJO_M, final=10.8),
   dict(name="MERY GÓMEZ POZOS", rgb=ROJO_M, final=7.4),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=6.8),
   dict(name="MARIANA FERNÁNDEZ RAMÍREZ", rgb=ROJO_M, final=5.4),
   dict(name="OTRO", rgb=GRIS, final=3.4)]),

 11: dict(muni="Guadalajara", tipo="PRECANDIDATO", partido="MC", fechas=F12,
          x=(128, 1007), series=[
   dict(name="VERÓNICA DELGADILLO GARCÍA", rgb=NAR, final=39.6),
   dict(name="CLEMENTE CASTAÑEDA HOEFLICH", rgb=NAR, final=21.7),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=18.8),
   dict(name="OTRO", rgb=GRIS, final=17.1),
   dict(name="MANUEL ROMO PARRA", rgb=NAR, final=2.8)]),

 13: dict(muni="Guadalajara", tipo="REELECCION", partido="MC", fechas=F12,
          x=(128, 1007), series=[
   dict(name="NO", rgb=(200, 20, 20), final=59.8),
   dict(name="SÍ", rgb=(0, 15, 70), final=40.2)]),

 73: dict(muni="Zapopan", tipo="INTENCION_PARTIDO", partido=None, fechas=F13,
          x=(124, 1010), series=[
   dict(name="MORENA", rgb=ROJO_M, final=29.7), dict(name="MC", rgb=NAR, final=26.3),
   dict(name="PAN", rgb=AZUL, final=17.2), dict(name="PRI", rgb=ROJO_P, final=11.6),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=10.5), dict(name="PT", rgb=AMA, final=2.8),
   dict(name="PVEM", rgb=VER, final=1.9)]),

 75: dict(muni="Zapopan", tipo="PRECANDIDATO", partido="PAN", fechas=F12,
          x=(128, 1007), series=[
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=35.1),
   dict(name="OTRO", rgb=GRIS, final=27.4),
   dict(name="OMAR BORBOA", rgb=AZUL, final=20.8),
   dict(name="JERÓNIMO DÍAZ OROZCO", rgb=AZUL, final=16.7)]),

 77: dict(muni="Zapopan", tipo="PRECANDIDATO", partido="PRI", fechas=F12,
          x=(128, 1007), series=[
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=26.8),
   dict(name="ALONDRA GETSEMANY FAUSTO DE LEÓN", rgb=ROJO_P, final=26.2),
   dict(name="ANDREA MÁRQUEZ VILLARREAL", rgb=ROJO_P, final=23.8),
   dict(name="OTRO", rgb=GRIS, final=23.2)]),

 79: dict(muni="Zapopan", tipo="PRECANDIDATO", partido="MORENA", fechas=F12,
          x=(128, 1007), series=[
   dict(name="PEDRO KUMAMOTO", rgb=ROJO_M, final=38.2),
   dict(name="MAURO LOMELÍ", rgb=ROJO_M, final=16.9),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=16.2),
   dict(name="GABRIELA FRANCO", rgb=ROJO_M, final=11.8),
   dict(name="OTRO", rgb=GRIS, final=10.3),
   dict(name="KARIME MORQUECHO", rgb=ROJO_M, final=3.7, start=6),
   dict(name="MARÍA REYNOSO", rgb=ROJO_M, final=2.9, start=6)]),

 81: dict(muni="Zapopan", tipo="PRECANDIDATO", partido="MC", fechas=F12,
          x=(128, 1007), series=[
   dict(name="GABRIELA CÁRDENAS RODRÍGUEZ", rgb=NAR, final=24.6),
   dict(name="AÚN NO DECIDE", rgb=NEGRO, final=20.3),
   dict(name="MÓNICA MAGAÑA", rgb=NAR, final=18.6),
   dict(name="OTRO", rgb=GRIS, final=17.8),
   dict(name="ÓSCAR JAVIER RAMÍREZ CASTELLANOS", rgb=NAR, final=10.2),
   dict(name="MIRZA FLORES GÓMEZ", rgb=NAR, final=8.5)]),
}

BARRAS = {
 2:  ("Guadalajara", "INTENCION_PARTIDO", None, [("MORENA",32.7),("MC",22.1),("PAN",12.9),
      ("PRI",10.6),("PT",3.6),("PVEM",1.7),("AÚN NO DECIDE",16.4)]),
 4:  ("Guadalajara","PRECANDIDATO","PAN",[("MIGUEL ÁNGEL MONRAZ IBARRA",21.4),
      ("DIANA ARACELI GONZÁLEZ MARTÍNEZ",16.1),("JOSÉ MIGUEL MENDOZA LARA",14.9),
      ("PAOLA ESPINOSA SÁNCHEZ",7.1),("CÉSAR MADRIGAL DÍAZ",3.6),("OTRO",20.2),
      ("AÚN NO DECIDE",16.7)]),
 6:  ("Guadalajara","PRECANDIDATO","PRI",[("LAURA HARO RAMÍREZ",31.5),
      ("HORTENSIA NOROÑA QUEZADA",13.7),("VERÓNICA FLORES PÉREZ",10.7),("OTRO",26.8),
      ("AÚN NO DECIDE",17.3)]),
 8:  ("Guadalajara","PRECANDIDATO","MORENA",[("CARLOS LOMELÍ BOLAÑOS",35.8),
      ("CHEMA MARTÍNEZ",16.2),("ITZUL BARRERA RODRÍGUEZ",14.2),
      ("CARLOS PALACIOS RODRÍGUEZ",10.8),("MERY GÓMEZ POZOS",7.4),
      ("MARIANA FERNÁNDEZ RAMÍREZ",5.4),("OTRO",3.4),("AÚN NO DECIDE",6.8)]),
 10: ("Guadalajara","PRECANDIDATO","MC",[("VERÓNICA DELGADILLO GARCÍA",39.6),
      ("CLEMENTE CASTAÑEDA HOEFLICH",21.7),("MANUEL ROMO PARRA",2.8),("OTRO",17.1),
      ("AÚN NO DECIDE",18.8)]),
 12: ("Guadalajara","REELECCION","MC",[("SÍ",40.2),("NO",59.8)]),
 72: ("Zapopan","INTENCION_PARTIDO",None,[("MORENA",29.7),("MC",26.3),("PAN",17.2),
      ("PRI",11.6),("PT",2.8),("PVEM",1.9),("AÚN NO DECIDE",10.5)]),
 74: ("Zapopan","PRECANDIDATO","PAN",[("OMAR BORBOA",20.8),("JERÓNIMO DÍAZ OROZCO",16.7),
      ("OTRO",27.4),("AÚN NO DECIDE",35.1)]),
 76: ("Zapopan","PRECANDIDATO","PRI",[("ALONDRA GETSEMANY FAUSTO DE LEÓN",26.2),
      ("ANDREA MÁRQUEZ VILLARREAL",23.8),("OTRO",23.2),("AÚN NO DECIDE",26.8)]),
 78: ("Zapopan","PRECANDIDATO","MORENA",[("PEDRO KUMAMOTO",38.2),("MAURO LOMELÍ",16.9),
      ("GABRIELA FRANCO",11.8),("KARIME MORQUECHO",3.7),("MARÍA REYNOSO",2.9),
      ("OTRO",10.3),("AÚN NO DECIDE",16.2)]),
 80: ("Zapopan","PRECANDIDATO","MC",[("GABRIELA CÁRDENAS RODRÍGUEZ",24.6),
      ("MÓNICA MAGAÑA",18.6),("ÓSCAR JAVIER RAMÍREZ CASTELLANOS",10.2),
      ("MIRZA FLORES GÓMEZ",8.5),("OTRO",17.8),("AÚN NO DECIDE",20.3)]),
}

# Anclas fijadas por lectura visual ampliada (marcadores del mismo color fusionados)
OVERRIDE = {
 5: {"MIGUEL ÁNGEL MONRAZ IBARRA": 439.0, "DIANA ARACELI GONZÁLEZ MARTÍNEZ": 490.0,
     "JOSÉ MIGUEL MENDOZA LARA": 501.0, "PAOLA ESPINOSA SÁNCHEZ": 574.5,
     "CÉSAR MADRIGAL DÍAZ": 607.5},
 9: {"CARLOS LOMELÍ BOLAÑOS": 340.5, "CHEMA MARTÍNEZ": 505.5,
     "ITZUL BARRERA RODRÍGUEZ": 522.5, "CARLOS PALACIOS RODRÍGUEZ": 551.0,
     "MERY GÓMEZ POZOS": 579.0, "MARIANA FERNÁNDEZ RAMÍREZ": 596.5},
}

# Correcciones manuales verificadas por inspeccion visual ampliada (marcador ocluido)
MANUAL = {
 (3, "PRI", "2026-03-12"): (11.9, "Marcador oculto tras la serie AÚN NO DECIDE; leído por ampliación"),
 (3, "PVEM", "2025-08-12"): (2.5, "Marcador oculto tras PT; validado por residual 100-97.5"),
 (3, "PVEM", "2026-03-12"): (2.0, "Marcador adyacente a PT; validado por residual"),
 (3, "MC", "2025-08-12"): (16.2, "Marcador en borde del plano; lectura ampliada y=518.8, residual 16.1"),
 (3, "PAN", "2026-07-12"): (14.3, "Cruce exacto con AÚN NO DECIDE; lectura ampliada y=533.6, residual 14.3"),
 (73, "MC", "2025-08-12"): (23.3, "Marcador en borde del plano; lectura ampliada y=445.5, residual 23.3"),
}

def main():
    obs, incid = [], []
    for pg, (muni, tipo, partido, items) in BARRAS.items():
        for actor, pct in items:
            obs.append(dict(ola="2026-08-12", municipio=muni, tipo_pregunta=tipo,
                            partido_contexto=partido, actor=actor, valor_pct=pct,
                            pagina=pg, estatus="LITERAL", nota=""))

    for pg, cf in LAM.items():
        vals, err = run(pg, cf["series"], len(cf["fechas"]), cf["x"][0], cf["x"][1], box=BOX,
                        anchor_override=OVERRIDE.get(pg))
        incid.append(dict(pagina=pg, error_calibracion_pp=round(err, 3)))
        for s in cf["series"]:
            for i, fecha in enumerate(cf["fechas"]):
                v = vals[s["name"]][i]
                key = (pg, s["name"], fecha)
                est, nota = "PONDERADO", "Serie histórica sin etiqueta numérica en la fuente"
                if i == len(cf["fechas"]) - 1:
                    est, nota = "LITERAL", ""
                if key in MANUAL:
                    v, nota = MANUAL[key][0], MANUAL[key][1]
                    est = "PONDERADO"
                if v is None:
                    est, nota = "AUSENTE", "Marcador ocluido; no resuelto automáticamente"
                if i < s.get("start", 0):
                    continue
                obs.append(dict(ola=fecha, municipio=cf["muni"], tipo_pregunta=cf["tipo"],
                                partido_contexto=cf["partido"], actor=s["name"],
                                valor_pct=v, pagina=pg, estatus=est, nota=nota))

    json.dump(dict(observaciones=obs, calibracion=incid), open("registro_piloto.json", "w"),
              ensure_ascii=False, indent=1)
    n_aus = sum(1 for o in obs if o["estatus"] == "AUSENTE")
    print("observaciones:", len(obs), "| ausentes:", n_aus)
    print("calibracion max (pp):", max(c["error_calibracion_pp"] for c in incid))
    for o in obs:
        if o["estatus"] == "AUSENTE":
            print("  AUSENTE", o["pagina"], o["actor"], o["ola"])


if __name__ == "__main__":
    main()
