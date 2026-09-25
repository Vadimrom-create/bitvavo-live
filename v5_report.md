# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T07:33:54.339475+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T07:33:24.494446+00:00 | âge ticker : 145.0 s | durée : 147.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- APT-EUR : 0.7121 € ; score 90.65/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.134703 € ; score 89.66/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.67849 € ; score 89.24/100 ; SURVEILLE ; WICK_SETUP
- ROSE-EUR : 0.007049 € ; score 88.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- EPIC-EUR : 0.44192 € ; score 85.96/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 89.828 | +41.73 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.70279 | +41.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.102202 | +28.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.4877 | +27.70 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.050052 | +21.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.085677 | +18.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17863 | +18.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021514 | +17.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20249 | +15.29 % | DETECTED_EARLY | NONE | NONE |
| TAI-EUR | 0.004058 | +14.76 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1427 scans ; 610697 observations ; 817 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
