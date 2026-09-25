# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T01:34:00.089175+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T01:33:28.802600+00:00 | âge ticker : 152.3 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.27263 € ; score 88.16/100 ; SURVEILLE ; seuil achat non atteint
- RON-EUR : 0.054255 € ; score 86.38/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- SKL-EUR : 0.004041 € ; score 85.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GRASS-EUR : 0.39501 € ; score 84.67/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.029987 € ; score 84.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.061186 | +46.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.4658 | +29.30 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 78.456 | +27.38 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.62099 | +26.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.095403 | +21.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DYM-EUR | 0.01891 | +20.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021687 | +19.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.036502 | +18.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0082026 | +17.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 62.867 | +15.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1406 scans ; 601730 observations ; 791 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
