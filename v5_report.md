# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T04:29:54.913989+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T04:29:27.555957+00:00 | âge ticker : 141.1 s | durée : 141.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- AXS-EUR : 1.1339 € | IGNITION | score 83.70/100 | entrée 7.05/10
  Entrée 1.1339 € ; stop 1.0703 € ; TP1 1.261 € ; TP2 1.3246 € ; montant 190.80 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 4.443/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.7345 € ; score 88.86/100 ; SURVEILLE ; WICK_SETUP
- MOCA-EUR : 0.00943 € ; score 86.61/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- BLUR-EUR : 0.019585 € ; score 86.29/100 ; SURVEILLE ; SPREAD_RISK
- BNB-EUR : 681.65 € ; score 84.16/100 ; SURVEILLE ; WICK_SETUP
- ORCA-EUR : 1.58184 € ; score 84.14/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.072525 | +78.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032558 | +19.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.094751 | +19.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GALA-EUR | 0.0023175 | +11.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BAT-EUR | 0.08839 | +10.83 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| APE-EUR | 0.1494 | +10.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BIGTIME-EUR | 0.008717 | +10.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0058907 | +10.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1339 | +10.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.82999 | +9.76 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2027 scans ; 867488 observations ; 1597 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
