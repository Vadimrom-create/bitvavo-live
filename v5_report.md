# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T19:48:16.619403+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T19:47:44.808230+00:00 | âge ticker : 149.9 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.00795 € | IGNITION | score 93.41/100 | entrée 8.20/10
  Entrée 0.0079488 € ; stop 0.0075903 € ; TP1 0.0086658 € ; TP2 0.0090243 € ; montant 231.02 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.536/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.29194 € ; score 84.79/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25901 € ; score 83.77/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 103.031 € ; score 83.15/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.029636 € ; score 81.69/100 ; SURVEILLE ; seuil achat non atteint
- GRT-EUR : 0.020238 € ; score 80.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.018752 | +122.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0016482 | +114.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.05326 | +57.07 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.045649 | +39.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.110067 | +37.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30794 | +37.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.001063 | +35.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008415 | +29.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.33001 | +24.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.321e-06 | +23.70 % | DETECTED_EARLY | NONE | NONE |

Historique : 1107 scans ; 474319 observations ; 404 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
