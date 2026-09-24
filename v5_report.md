# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T03:00:55.374578+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T03:00:30.501815+00:00 | âge ticker : 142.0 s | durée : 143.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- FARTCOIN-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- EIGEN-EUR : 0.21217 € | IGNITION | score 86.82/100 | entrée 6.80/10
  Entrée 0.21181 € ; stop 0.20431 € ; TP1 0.22681 € ; TP2 0.23431 € ; montant 250.00 € ; risque théorique 10.57 € ; R/R net 1.50.
  Chase risk : 4.126/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LTC-EUR : 57.643 € | IGNITION | score 83.73/100 | entrée 6.60/10
  Entrée 57.732 € ; stop 53.966 € ; TP1 65.264 € ; TP2 69.03 € ; montant 166.66 € ; risque théorique 12.00 € ; R/R net 1.71.
  Chase risk : 8.278/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BONK-EUR : 3.1454e-06 € ; score 91.56/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZK-EUR : 0.010158 € ; score 90.94/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- A-EUR : 0.081671 € ; score 90.79/100 ; SURVEILLE ; seuil achat non atteint
- ARK-EUR : 0.14055 € ; score 90.20/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ETC-EUR : 7.8809 € ; score 89.15/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021029 | +36.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.118569 | +35.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.0415 | +19.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.029698 | +14.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3892 | +11.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018099 | +11.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.76607 | +9.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0018397 | +9.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOSO-EUR | 0.2881 | +8.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| KMNO-EUR | 0.032917 | +8.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1323 scans ; 566335 observations ; 679 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
