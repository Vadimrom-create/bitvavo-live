# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T00:51:29.479983+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T00:50:57.997182+00:00 | âge ticker : 146.8 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LINK-EUR : 12.3052 € ; score 94.67/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.140655 € ; score 89.78/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KERNEL-EUR : 0.049249 € ; score 89.32/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- AAVE-EUR : 135.66 € ; score 87.23/100 ; SURVEILLE ; WICK_SETUP
- RPL-EUR : 1.8724 € ; score 86.74/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0013919 | +78.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.074564 | +67.15 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EDGE-EUR | 0.103213 | +37.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.21822 | +28.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065937 | +19.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.73306 | +18.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.45458 | +17.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.70915 | +17.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.23684 | +16.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.033951 | +16.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1489 scans ; 637171 observations ; 916 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
