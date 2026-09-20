# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T15:46:42.815566+00:00
État : OK | marchés EUR : 426 | V4 : 385 | données valides : 32
Récupération : 2026-09-20T15:46:14.526894+00:00 | âge ticker : 150.3 s | durée : 151.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 34/426 ; 15 min 73/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : INVALID_5M
- RENDER-EUR : WICK_SETUP, INVALID_15M, INVALID_5M

## SURVEILLE

- LINK-EUR : 10.7 € ; score 85.23/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 79.761 € ; score 78.12/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.73142 € ; score 76.16/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.20739 € ; score 74.93/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- PEPE-EUR : 3.4423e-06 € ; score 73.99/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.003466 | +62.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.028754 | +30.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.7693 | +19.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| C-EUR | 0.069329 | +18.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007147 | +18.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.47931 | +17.18 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ALGO-EUR | 0.098085 | +11.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.025326 | +10.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SKL-EUR | 0.0038019 | +9.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.030193 | +8.18 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 992 scans ; 425329 observations ; 230 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
