# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T02:20:20.244068+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-01T02:19:46.049519+00:00 | âge ticker : 160.4 s | durée : 162.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.972 € ; score 85.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CVX-EUR : 1.9238 € ; score 84.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- REZ-EUR : 0.0042012 € ; score 81.32/100 ; SURVEILLE ; seuil achat non atteint
- DEEP-EUR : 0.020785 € ; score 81.19/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- C-EUR : 0.080529 € ; score 81.05/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0261 | +87.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.36507 | +52.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.43457 | +30.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.43789 | +26.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008387 | +24.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33164 | +20.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.027943 | +17.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICX-EUR | 0.0074 | +14.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0603227 | +13.94 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZBCN-EUR | 0.0025008 | +12.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1879 scans ; 804048 observations ; 1431 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
