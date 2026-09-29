# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T11:23:21.262849+00:00
État : OK | marchés EUR : 429 | V4 : 396 | données valides : 428
Récupération : 2026-09-29T11:22:51.030017+00:00 | âge ticker : 146.9 s | durée : 147.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : SPREAD_RISK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JTO-EUR : 0.4966 € ; score 90.10/100 ; SURVEILLE ; WICK_SETUP
- XVG-EUR : 0.0028531 € ; score 89.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SUSHI-EUR : 0.23645 € ; score 87.34/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- WELL-EUR : 0.0020498 € ; score 87.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SENT-EUR : 0.018689 € ; score 86.45/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018238 | +44.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0023 | +28.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.27869 | +26.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.100382 | +25.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.4606 | +22.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.60561 | +21.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.22273 | +20.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.34611 | +19.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.088156 | +15.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0271 | +14.81 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1765 scans ; 755095 observations ; 1307 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
