# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T11:01:41.190172+00:00
État : OK | marchés EUR : 429 | V4 : 396 | données valides : 428
Récupération : 2026-09-29T11:01:12.585481+00:00 | âge ticker : 149.3 s | durée : 150.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.0163358 € ; score 91.89/100 ; SURVEILLE ; WICK_SETUP
- CFG-EUR : 0.143413 € ; score 90.82/100 ; SURVEILLE ; WICK_SETUP
- IO-EUR : 0.1435 € ; score 87.34/100 ; SURVEILLE ; WICK_SETUP
- ZAMA-EUR : 0.070427 € ; score 86.62/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ROSE-EUR : 0.007919 € ; score 85.75/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018516 | +51.08 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CELO-EUR | 0.102846 | +28.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.60572 | +24.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 11.5208 | +23.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.267 | +21.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34761 | +19.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21983 | +19.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.002123 | +18.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVX-EUR | 2.057 | +16.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.086505 | +14.78 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1764 scans ; 754666 observations ; 1307 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
