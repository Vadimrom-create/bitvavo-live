# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T05:23:29.754307+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 427
Récupération : 2026-09-28T05:22:54.497421+00:00 | âge ticker : 156.5 s | durée : 157.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- KAS-EUR : 0.04184 € | IGNITION | score 82.93/100 | entrée 7.25/10
  Entrée 0.04192 € ; stop 0.040157 € ; TP1 0.045446 € ; TP2 0.047209 € ; montant 245.35 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 1.849/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.50614 € | IGNITION | score 80.62/100 | entrée 6.95/10
  Entrée 0.50655 € ; stop 0.48774 € ; TP1 0.54416 € ; TP2 0.56297 € ; montant 250.00 € ; risque théorique 11.00 € ; R/R net 1.52.
  Chase risk : 1.736/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LRC-EUR : 0.00932 € ; score 89.68/100 ; SURVEILLE ; WICK_SETUP
- GLMR-EUR : 0.006916 € ; score 88.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- XDC-EUR : 0.02913 € ; score 78.36/100 ; SURVEILLE ; seuil achat non atteint
- ELSA-EUR : 0.053475 € ; score 78.28/100 ; SURVEILLE ; SPREAD_RISK
- WLD-EUR : 0.45961 € ; score 76.19/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 222.829 | +35.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.10047 | +28.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016354 | +27.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.028559 | +18.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0045452 | +18.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.31052 | +15.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.016966 | +13.33 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SEI-EUR | 0.071509 | +12.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.29109 | +10.41 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| GRASS-EUR | 0.55058 | +9.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1674 scans ; 716166 observations ; 1236 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
