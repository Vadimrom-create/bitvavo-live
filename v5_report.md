# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T07:55:03.136047+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T07:54:36.584922+00:00 | âge ticker : 143.5 s | durée : 144.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.38884 € | IGNITION | score 87.72/100 | entrée 7.45/10
  Entrée 0.38888 € ; stop 0.37488 € ; TP1 0.41688 € ; TP2 0.43088 € ; montant 250.00 € ; risque théorique 10.72 € ; R/R net 1.51.
  Chase risk : 4.276/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- T-EUR : 0.0050525 € ; score 91.23/100 ; SURVEILLE ; SPREAD_RISK
- TAO-EUR : 257.49 € ; score 90.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.39 € ; score 90.03/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SAFE-EUR : 0.095576 € ; score 89.81/100 ; SURVEILLE ; LOW_LIQUIDITY
- HYPE-EUR : 82.484 € ; score 89.63/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.002325 | +53.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.37768 | +37.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.11321 | +19.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.85925 | +18.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019454 | +12.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOSO-EUR | 0.28859 | +10.65 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CELR-EUR | 0.0028492 | +10.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 60.503 | +9.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACU-EUR | 0.11543 | +8.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.353 | +8.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1339 scans ; 573151 observations ; 694 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
