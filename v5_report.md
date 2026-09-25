# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T08:04:52.060581+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T08:04:25.808628+00:00 | âge ticker : 143.3 s | durée : 144.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RENDER-EUR : 1.6364 € ; score 92.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 62.861 € ; score 91.98/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.39 € ; score 91.06/100 ; SURVEILLE ; SPREAD_RISK
- ALGO-EUR : 0.100265 € ; score 90.31/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PROM-EUR : 4.9053 € ; score 89.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.74542 | +50.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 89.603 | +42.10 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.49787 | +29.65 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.101218 | +26.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.18711 | +23.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08735 | +20.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021515 | +18.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.04881 | +18.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.038 | +17.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TAI-EUR | 0.004048 | +15.49 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1429 scans ; 611551 observations ; 817 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
