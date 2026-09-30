# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T11:23:02.497026+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T11:22:32.693594+00:00 | âge ticker : 148.9 s | durée : 149.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WIF-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.10999 € ; score 93.72/100 ; SURVEILLE ; WICK_SETUP
- NEO-EUR : 2.2715 € ; score 88.34/100 ; SURVEILLE ; STABILITY_HOLD
- ZAMA-EUR : 0.064857 € ; score 85.96/100 ; SURVEILLE ; WICK_SETUP
- NOT-EUR : 0.00043746 € ; score 84.69/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- RON-EUR : 0.057004 € ; score 83.80/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5933 | +77.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.38277 | +60.15 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ARK-EUR | 0.3 | +39.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.39847 | +33.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 275.357 | +24.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008115 | +21.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.093833 | +21.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.391 | +19.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.067196 | +18.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.87616 | +12.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1836 scans ; 785558 observations ; 1369 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
