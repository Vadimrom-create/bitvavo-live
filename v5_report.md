# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T11:58:31.455693+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 35
Récupération : 2026-09-19T11:58:02.673883+00:00 | âge ticker : 149.4 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/427 ; 15 min 80/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- CAKE-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INVALID_5M
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : CHASE_RISK, INVALID_5M
- POL-EUR : INVALID_5M
- PYTH-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- RENDER-EUR : STABILITY_HOLD, INVALID_5M
- VET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FET-EUR : 0.16012 € ; score 91.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 0.9895 € ; score 90.86/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.19753 € ; score 87.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 235 € ; score 87.30/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.6524 € ; score 85.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.065648 | +37.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.079262 | +37.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.211438 | +33.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.023766 | +32.84 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.038718 | +31.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.146458 | +28.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0037007 | +28.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.38762 | +23.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.28955 | +23.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0569594 | +18.14 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 887 scans ; 380528 observations ; 195 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
