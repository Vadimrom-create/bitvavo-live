# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T01:05:35.518259+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T01:05:02.722835+00:00 | âge ticker : 156.1 s | durée : 156.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 137.41 € ; score 93.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MANA-EUR : 0.080487 € ; score 92.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HOT-EUR : 0.000394 € ; score 88.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PENGU-EUR : 0.0091391 € ; score 88.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RPL-EUR : 1.8715 € ; score 85.64/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.077422 | +72.63 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0013255 | +69.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.103345 | +37.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.22125 | +25.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.066609 | +18.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.72745 | +17.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.45499 | +16.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.70467 | +15.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.013254 | +15.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.49938 | +14.67 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1490 scans ; 637598 observations ; 917 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
