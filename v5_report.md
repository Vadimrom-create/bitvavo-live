# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-16T04:52:08.125488+00:00
État : OK | marchés EUR : 429 | V4 : 387 | données valides : 7
Récupération : 2026-09-16T04:51:39.147490+00:00 | âge ticker : 143.1 s | durée : 144.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 18/429 ; 15 min 34/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- BCH-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00062966 € ; score 86.46/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 2.9456e-06 € ; score 85.35/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.12868 € ; score 82.55/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2083.03 € ; score 78.58/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.16956 € ; score 77.49/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.43867 | +34.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.089119 | +27.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.32949 | +22.25 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ARB-EUR | 0.13561 | +17.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALIGN-EUR | 0.005767 | +12.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LAPTOP-EUR | 0.20746 | +11.79 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| USELESS-EUR | 0.19704 | +11.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FOLD-EUR | 0.044967 | +10.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| GLMR-EUR | 0.005114 | +9.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.022272 | +8.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 606 scans ; 260000 observations ; 99 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
