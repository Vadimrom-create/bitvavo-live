# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T10:56:56.456752+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T10:56:22.315828+00:00 | âge ticker : 150.9 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- ETC-EUR : 8.3083 € | IGNITION | score 85.64/100 | entrée 6.85/10
  Entrée 8.3263 € ; stop 8.0318 € ; TP1 8.9152 € ; TP2 9.2097 € ; montant 250.00 € ; risque théorique 10.56 € ; R/R net 1.50.
  Chase risk : 0.624/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GOAT-EUR : 0.01679 € ; score 90.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BEAM-EUR : 0.001817 € ; score 88.92/100 ; SURVEILLE ; SPREAD_RISK
- CELO-EUR : 0.07804 € ; score 86.33/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- AVNT-EUR : 0.09668 € ; score 86.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- DRIFT-EUR : 0.016002 € ; score 83.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021359 | +37.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.11533 | +34.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IMU-EUR | 0.0020875 | +22.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.34061 | +19.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21822 | +14.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.3919 | +10.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.29164 | +10.92 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CVC-EUR | 0.02731 | +9.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.15193 | +7.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LTC-EUR | 58.767 | +6.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1349 scans ; 577411 observations ; 712 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
