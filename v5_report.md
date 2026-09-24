# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T12:52:55.892520+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T12:52:21.642712+00:00 | âge ticker : 152.8 s | durée : 153.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : 65.942 € | IGNITION | score 87.19/100 | entrée 6.75/10
  Entrée 65.999 € ; stop 62.615 € ; TP1 72.766 € ; TP2 76.15 € ; montant 206.56 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.252/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FET-EUR : 0.17488 € ; score 87.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENS-EUR : 6.0567 € ; score 86.96/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 58.106 € ; score 83.32/100 ; SURVEILLE ; WICK_SETUP
- OP-EUR : 0.10942 € ; score 81.05/100 ; SURVEILLE ; WICK_SETUP
- INIT-EUR : 0.083448 € ; score 80.83/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021261 | +36.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.35902 | +29.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.108335 | +25.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.21701 | +16.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.045609 | +9.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.034392 | +8.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.154 | +8.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28477 | +8.30 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| IMU-EUR | 0.0018893 | +8.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.026617 | +7.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1356 scans ; 580393 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
