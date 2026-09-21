# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T12:35:52.787997+00:00
État : OK | marchés EUR : 426 | V4 : 392 | données valides : 426
Récupération : 2026-09-21T12:35:20.604355+00:00 | âge ticker : 155.9 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AERO-EUR : 0.59975 € ; score 87.27/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.030192 € ; score 85.84/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.07966 € ; score 84.17/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 53.874 € ; score 82.99/100 ; SURVEILLE ; WICK_SETUP
- PENDLE-EUR : 2.3685 € ; score 82.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.05697 | +72.55 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.051678 | +65.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.00101 | +38.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.056901 | +31.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.05384 | +30.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030914 | +29.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23142 | +26.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.095306 | +26.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 0.89577 | +25.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CETUS-EUR | 0.025265 | +24.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1076 scans ; 461113 observations ; 357 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
