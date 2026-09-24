# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T15:56:41.752852+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 426
Récupération : 2026-09-24T15:56:06.879715+00:00 | âge ticker : 149.1 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : 0.098526 € | IGNITION | score 83.02/100 | entrée 6.85/10
  Entrée 0.098642 € ; stop 0.094435 € ; TP1 0.107055 € ; TP2 0.111262 € ; montant 242.42 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.85/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- JUP-EUR : 0.26818 € | IGNITION | score 80.59/100 | entrée 6.95/10
  Entrée 0.26852 € ; stop 0.25648 € ; TP1 0.29259 € ; TP2 0.30463 € ; montant 232.19 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.214/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DBR-EUR : 0.017809 € ; score 91.41/100 ; SURVEILLE ; WICK_SETUP
- FLOKI-EUR : 2.5158e-05 € ; score 87.34/100 ; SURVEILLE ; seuil achat non atteint
- WOO-EUR : 0.011178 € ; score 86.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MOG-EUR : 1.093e-07 € ; score 85.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- SNX-EUR : 0.21983 € ; score 84.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0020728 | +41.18 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.3421 | +30.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45432 | +25.64 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 65.564 | +25.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22876 | +19.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10036 | +19.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.035599 | +18.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.000913 | +18.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FET-EUR | 0.19858 | +16.70 % | DETECTED_EARLY | NONE | NONE |
| ETC-EUR | 8.8913 | +15.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1366 scans ; 584653 observations ; 718 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
