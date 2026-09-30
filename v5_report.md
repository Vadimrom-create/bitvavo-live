# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T17:59:17.209169+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T17:58:39.906820+00:00 | âge ticker : 170.6 s | durée : 171.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- PUMP-EUR : 0.0051917 € | IGNITION | score 81.65/100 | entrée 7.25/10
  Entrée 0.0051892 € ; stop 0.0049046 € ; TP1 0.0057583 € ; TP2 0.0060429 € ; montant 194.64 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 4.413/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LQTY-EUR : 0.20945 € ; score 88.47/100 ; SURVEILLE ; SPREAD_RISK
- TRB-EUR : 18.2 € ; score 88.31/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SHIB-EUR : 5.0742e-06 € ; score 87.35/100 ; SURVEILLE ; seuil achat non atteint
- JASMY-EUR : 0.0044779 € ; score 87.33/100 ; SURVEILLE ; WICK_SETUP
- ETHFI-EUR : 0.69708 € ; score 84.29/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5056 | +58.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.33826 | +41.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| UP-EUR | 0.08249 | +35.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43731 | +23.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 267.116 | +19.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007879 | +18.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0020985 | +17.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.028388 | +15.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.068136 | +14.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.31587 | +12.82 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1854 scans ; 793298 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
