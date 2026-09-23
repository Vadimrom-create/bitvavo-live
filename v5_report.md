# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T05:35:21.633420+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-23T05:34:49.366131+00:00 | âge ticker : 147.8 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NPC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CHZ-EUR : 0.0149 € ; score 91.60/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- F-EUR : 0.0033453 € ; score 90.87/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- TRB-EUR : 17.876 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PUMP-EUR : 0.0039342 € ; score 88.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0035422 € ; score 88.61/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.089796 | +45.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31294 | +32.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.306866 | +30.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.031572 | +30.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 296.51 | +29.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.4812 | +26.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.019477 | +25.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PENGU-EUR | 0.0094389 | +23.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16155 | +23.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.238 | +20.95 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1246 scans ; 533533 observations ; 599 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
