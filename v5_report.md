# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T15:38:56.036777+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-25T15:38:22.352507+00:00 | âge ticker : 166.3 s | durée : 168.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.28682 € | IGNITION | score 83.45/100 | entrée 7.30/10
  Entrée 0.28629 € ; stop 0.27507 € ; TP1 0.30873 € ; TP2 0.31995 € ; montant 250.00 € ; risque théorique 11.51 € ; R/R net 1.54.
  Chase risk : 2.372/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PYTH-EUR : 0.064453 € ; score 90.18/100 ; SURVEILLE ; seuil achat non atteint
- ILV-EUR : 3.3594 € ; score 88.78/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- LDO-EUR : 0.40085 € ; score 84.69/100 ; SURVEILLE ; seuil achat non atteint
- CYBER-EUR : 0.30059 € ; score 84.43/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- KITE-EUR : 0.11526 € ; score 84.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.06648 | +50.50 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.68471 | +38.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.014859 | +29.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19795 | +26.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08667 | +19.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037234 | +16.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22306 | +16.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 83.106 | +15.52 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.4375 | +15.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.117452 | +15.03 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1453 scans ; 621799 observations ; 870 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
