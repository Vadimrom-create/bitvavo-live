# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T21:39:26.445222+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T21:38:50.618315+00:00 | âge ticker : 151.6 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZRO-EUR : 1.5003 € ; score 87.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- LTC-EUR : 58.863 € ; score 85.73/100 ; SURVEILLE ; seuil achat non atteint
- MMT-EUR : 0.16633 € ; score 85.64/100 ; SURVEILLE ; seuil achat non atteint
- TWT-EUR : 0.54366 € ; score 84.80/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- ZIL-EUR : 0.003107 € ; score 84.08/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8615 | +76.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34303 | +43.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008362 | +22.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.4321 | +20.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.015795 | +16.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0606379 | +15.25 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PHA-EUR | 0.069094 | +14.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.32032 | +13.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOMI-EUR | 0.20123 | +13.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.44231 | +12.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1865 scans ; 798028 observations ; 1422 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
