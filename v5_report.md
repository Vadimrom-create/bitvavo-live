# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T21:56:29.343312+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-29T21:55:59.519756+00:00 | âge ticker : 146.1 s | durée : 147.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.4219 € | IGNITION | score 88.54/100 | entrée 6.95/10
  Entrée 1.4258 € ; stop 1.3687 € ; TP1 1.5399 € ; TP2 1.597 € ; montant 250.00 € ; risque théorique 11.73 € ; R/R net 1.55.
  Chase risk : 3.253/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FIL-EUR : 0.94737 € ; score 90.13/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.20875 € ; score 87.91/100 ; SURVEILLE ; WICK_SETUP
- XPL-EUR : 0.085575 € ; score 86.17/100 ; SURVEILLE ; WICK_SETUP
- BCH-EUR : 273.25 € ; score 86.14/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.0629 € ; score 84.78/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016781 | +29.36 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65083 | +28.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.07 | +27.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.28722 | +21.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35921 | +19.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021108 | +18.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051167 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.060338 | +15.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0353 | +15.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 146.79 | +14.36 % | DETECTED_EARLY | NONE | NONE |

Historique : 1796 scans ; 768394 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
