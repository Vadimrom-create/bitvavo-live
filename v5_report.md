# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T23:24:48.998566+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T23:24:14.740434+00:00 | âge ticker : 156.4 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETHFI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZRO-EUR : 1.4898 € | IGNITION | score 86.83/100 | entrée 5.80/10
  Entrée 1.4906 € ; stop 1.4089 € ; TP1 1.6539 € ; TP2 1.7356 € ; montant 194.75 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 9.173/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WIN-EUR : 4.1412e-05 € ; score 87.12/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- BONK-EUR : 3.2364e-06 € ; score 85.80/100 ; SURVEILLE ; seuil achat non atteint
- REZ-EUR : 0.0038148 € ; score 85.70/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.007967 € ; score 83.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- YB-EUR : 0.07912 € ; score 82.93/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GRASS-EUR | 0.68085 | +31.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.00166 | +31.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.36097 | +30.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0793 | +27.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002254 | +27.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0052129 | +21.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.064349 | +20.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRIA-EUR | 0.004028 | +14.95 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.090065 | +14.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 235.085 | +13.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1801 scans ; 770539 observations ; 1341 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
