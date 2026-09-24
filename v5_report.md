# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T16:36:59.310315+00:00
État : OK | marchés EUR : 426 | V4 : 385 | données valides : 426
Récupération : 2026-09-24T16:36:27.897676+00:00 | âge ticker : 153.1 s | durée : 154.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.18639 € | IGNITION | score 90.98/100 | entrée 7.90/10
  Entrée 0.18593 € ; stop 0.17832 € ; TP1 0.20115 € ; TP2 0.20876 € ; montant 250.00 € ; risque théorique 11.95 € ; R/R net 1.56.
  Chase risk : 7.149/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MAVIA-EUR : 0.030523 € ; score 91.36/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.100895 € ; score 88.76/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.084791 € ; score 86.36/100 ; SURVEILLE ; CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- ORCA-EUR : 1.39996 € ; score 85.65/100 ; SURVEILLE ; WICK_SETUP
- IMX-EUR : 0.13583 € ; score 85.62/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021272 | +42.58 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.34671 | +31.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.455 | +25.24 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 64.917 | +22.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10216 | +20.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.036171 | +18.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0161828 | +18.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 74.003 | +17.37 % | DETECTED_EARLY | NONE | NONE |
| FET-EUR | 0.20048 | +17.11 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.088989 | +17.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1368 scans ; 585505 observations ; 725 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
