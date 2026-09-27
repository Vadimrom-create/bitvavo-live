# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T10:55:20.302986+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T10:54:45.366019+00:00 | âge ticker : 154.0 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BRETT-EUR : 0.005581 € ; score 92.75/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GMT-EUR : 0.007962 € ; score 91.33/100 ; SURVEILLE ; seuil achat non atteint
- MAV-EUR : 0.011177 € ; score 91.12/100 ; SURVEILLE ; SPREAD_RISK
- SPK-EUR : 0.022106 € ; score 87.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- 0G-EUR : 0.23156 € ; score 85.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 150.653 | +60.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008854 | +51.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 1.07151 | +49.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.25959 | +37.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006308 | +35.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.121876 | +23.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006763 | +23.43 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006393 | +23.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.55887 | +21.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.50003 | +17.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1610 scans ; 688838 observations ; 1121 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
