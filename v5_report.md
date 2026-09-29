# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T15:49:16.249377+00:00
État : OK | marchés EUR : 429 | V4 : 396 | données valides : 428
Récupération : 2026-09-29T15:48:36.855480+00:00 | âge ticker : 160.8 s | durée : 162.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MOVR-EUR : 0.9287 € ; score 89.33/100 ; SURVEILLE ; seuil achat non atteint
- JASMY-EUR : 0.0046916 € ; score 81.62/100 ; SURVEILLE ; SPREAD_RISK
- GALA-EUR : 0.0020074 € ; score 80.19/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 13.0646 € ; score 79.69/100 ; SURVEILLE ; WICK_SETUP
- DBR-EUR : 0.019089 € ; score 78.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017756 | +43.30 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.30605 | +41.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022604 | +27.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.59555 | +23.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35351 | +22.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.096388 | +17.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 150.49 | +17.27 % | DETECTED_EARLY | NONE | NONE |
| SYRUP-EUR | 0.21724 | +16.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.094365 | +16.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 2.9876 | +14.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1777 scans ; 760243 observations ; 1321 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
