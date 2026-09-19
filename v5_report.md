# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T08:52:29.118671+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 35
Récupération : 2026-09-19T08:51:59.064245+00:00 | âge ticker : 154.1 s | durée : 155.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/427 ; 15 min 72/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- JUP-EUR : WICK_SETUP, INVALID_5M
- KAS-EUR : WICK_SETUP, INVALID_5M
- PORTAL-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAO-EUR : 223.96 € ; score 85.30/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 7.572 € ; score 82.55/100 ; SURVEILLE ; seuil achat non atteint
- DOT-EUR : 0.9717 € ; score 80.24/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.358 € ; score 79.73/100 ; SURVEILLE ; WICK_SETUP
- PLUME-EUR : 0.0125217 € ; score 77.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.239768 | +53.08 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.068565 | +42.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.077999 | +35.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.151091 | +32.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.00369 | +27.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29394 | +25.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046125 | +23.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.5777 | +21.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.0225 | +19.47 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EPIC-EUR | 0.37641 | +19.31 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 875 scans ; 375404 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
