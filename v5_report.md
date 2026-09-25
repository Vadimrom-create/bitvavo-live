# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T14:58:37.557436+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T14:58:01.323516+00:00 | âge ticker : 167.1 s | durée : 168.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CFG-EUR : 0.136457 € ; score 87.81/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.4327 € ; score 86.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.063398 € ; score 85.19/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.12195 € ; score 83.70/100 ; SURVEILLE ; seuil achat non atteint
- ACU-EUR : 0.1185 € ; score 83.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.068164 | +57.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.7169 | +44.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19686 | +26.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038165 | +19.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 83.462 | +18.83 % | DETECTED_EARLY | NONE | NONE |
| DBR-EUR | 0.020946 | +18.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.117705 | +18.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.084631 | +17.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.095356 | +16.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.43711 | +16.49 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1451 scans ; 620945 observations ; 862 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
