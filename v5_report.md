# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T23:19:31.775862+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 30
Récupération : 2026-09-19T23:18:59.195798+00:00 | âge ticker : 158.4 s | durée : 159.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/427 ; 15 min 76/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- LTC-EUR : WICK_SETUP, INVALID_5M
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NPC-EUR : INVALID_5M
- PYTH-EUR : WICK_SETUP, INVALID_5M
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PEPE-EUR : 3.6036e-06 € ; score 81.76/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 79.92 € ; score 80.72/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 230.13 € ; score 80.66/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.75667 € ; score 79.89/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.36784 € ; score 79.58/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0029942 | +49.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.071866 | +41.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0089255 | +35.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 7.1751 | +25.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.073227 | +23.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.31552 | +23.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17916 | +21.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.615 | +20.82 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SKL-EUR | 0.0040278 | +16.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.137571 | +13.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 932 scans ; 399743 observations ; 222 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
