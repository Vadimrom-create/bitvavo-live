# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T11:13:41.972986+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-09-27T11:13:09.347541+00:00 | âge ticker : 152.2 s | durée : 153.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AUDIO-EUR : 0.01308 € ; score 90.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GMT-EUR : 0.007963 € ; score 90.38/100 ; SURVEILLE ; seuil achat non atteint
- ARKM-EUR : 0.12528 € ; score 90.08/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PENGU-EUR : 0.0089235 € ; score 88.75/100 ; SURVEILLE ; seuil achat non atteint
- BRETT-EUR : 0.0055749 € ; score 88.09/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 1.195 | +66.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 144.266 | +56.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008789 | +48.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AMP-EUR | 0.000646 | +40.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.25004 | +31.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.125 | +26.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.0062 | +19.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.006529 | +19.16 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WLD-EUR | 0.50061 | +17.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.5365 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1611 scans ; 689265 observations ; 1122 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
