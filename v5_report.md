# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T04:37:39.448304+00:00
État : OK | marchés EUR : 430 | V4 : 363 | données valides : 10
Récupération : 2026-09-18T04:37:10.641427+00:00 | âge ticker : 141.6 s | durée : 142.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/430 ; 15 min 45/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, STALE_DAILY_PROFILE
- DOGE-EUR : WICK_SETUP, INVALID_15M, STALE_DAILY_PROFILE
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- SYRUP-EUR : 0.18429 € ; score 87.17/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.233914 € ; score 78.76/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.3967 € ; score 77.38/100 ; SURVEILLE ; WIDE_SPREAD_RISK, WICK_SETUP
- LINK-EUR : 10.1735 € ; score 76.48/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 91.173 € ; score 74.16/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.23327 | +52.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.013826 | +34.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19253 | +32.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020119 | +29.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3 | +29.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.43418 | +28.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.53284 | +27.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00512 | +25.89 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| UNI-EUR | 7.4557 | +25.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.148313 | +23.61 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 767 scans ; 329204 observations ; 142 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
