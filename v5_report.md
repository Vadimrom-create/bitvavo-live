# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T00:02:55.246089+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-10-01T00:02:21.616675+00:00 | âge ticker : 147.7 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PUMP-EUR : 0.0052306 € ; score 90.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : 0.0044727 € ; score 89.15/100 ; SURVEILLE ; WICK_SETUP
- POL-EUR : 0.100479 € ; score 88.71/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 21.88 € ; score 88.16/100 ; SURVEILLE ; seuil achat non atteint
- DIA-EUR : 0.15051 € ; score 86.46/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.9077 | +72.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.362 | +51.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008398 | +22.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43738 | +19.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.027977 | +19.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.32741 | +16.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0611215 | +15.80 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOMI-EUR | 0.19733 | +12.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.37402 | +11.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.06935 | +11.28 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1873 scans ; 801468 observations ; 1428 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
