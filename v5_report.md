# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T22:51:29.091615+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T22:50:55.326944+00:00 | âge ticker : 150.9 s | durée : 151.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETHFI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZRO-EUR : 1.4485 € | IGNITION | score 89.45/100 | entrée 6.95/10
  Entrée 1.4502 € ; stop 1.3966 € ; TP1 1.5573 € ; TP2 1.6109 € ; montant 250.00 € ; risque théorique 10.96 € ; R/R net 1.52.
  Chase risk : 5.169/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CRV-EUR : 0.33422 € ; score 94.80/100 ; SURVEILLE ; WICK_SETUP
- DATAIP-EUR : 0.1966 € ; score 87.51/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 21.781 € ; score 85.38/100 ; SURVEILLE ; seuil achat non atteint
- RAY-EUR : 1.66091 € ; score 85.02/100 ; SURVEILLE ; seuil achat non atteint
- PNUT-EUR : 0.04655 € ; score 83.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017132 | +36.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66875 | +30.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0636 | +26.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.065774 | +24.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0051784 | +22.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0021687 | +22.00 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.28894 | +19.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35506 | +18.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDP-EUR | 0.021508 | +15.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRIA-EUR | 0.004013 | +14.53 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1799 scans ; 769681 observations ; 1340 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
