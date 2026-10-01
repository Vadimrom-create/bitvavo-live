# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T11:09:11.952633+00:00
État : OK | marchés EUR : 430 | V4 : 388 | données valides : 430
Récupération : 2026-10-01T11:08:36.073220+00:00 | âge ticker : 152.2 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DIA-EUR : 0.15186 € ; score 92.73/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.20049 € ; score 87.89/100 ; SURVEILLE ; seuil achat non atteint
- 1INCH-EUR : 0.089755 € ; score 85.14/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- SNX-EUR : 0.22354 € ; score 83.54/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- BCH-EUR : 273.13 € ; score 83.42/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00045 | +77.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5718 | +60.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0027168 | +38.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0665957 | +21.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.3379 | +20.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JASMY-EUR | 0.0054422 | +19.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028264 | +17.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.46589 | +15.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.1385 | +15.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| VELO-EUR | 0.0052091 | +15.52 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1904 scans ; 814798 observations ; 1477 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
