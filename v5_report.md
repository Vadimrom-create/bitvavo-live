# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T15:31:57.110171+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T15:31:27.388499+00:00 | âge ticker : 147.5 s | durée : 149.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.39896 € ; score 89.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.20626 € ; score 89.21/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- T-EUR : 0.0045904 € ; score 88.70/100 ; SURVEILLE ; LOW_LIQUIDITY
- CHZ-EUR : 0.01415 € ; score 87.97/100 ; SURVEILLE ; seuil achat non atteint
- BIO-EUR : 0.025358 € ; score 86.71/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01625 | +87.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FLOCK-EUR | 0.081991 | +31.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 283.46 | +23.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051043 | +23.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.070986 | +21.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.033216 | +15.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KITE-EUR | 0.11975 | +15.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVA-EUR | 0.2399 | +15.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.34411 | +14.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.45653 | +14.29 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1195 scans ; 511807 observations ; 509 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
