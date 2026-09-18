# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T08:58:26.745161+00:00
État : OK | marchés EUR : 430 | V4 : 367 | données valides : 11
Récupération : 2026-09-18T08:57:58.669510+00:00 | âge ticker : 143.0 s | durée : 144.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 40/430 ; 15 min 71/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STALE_DAILY_PROFILE
- FET-EUR : EXTENDED_24H, CHASE_RISK, STALE_DAILY_PROFILE
- INJ-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- KAS-EUR : INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : WICK_SETUP, INVALID_15M, STALE_DAILY_PROFILE
- SYRUP-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00058256 € ; score 86.44/100 ; SURVEILLE ; seuil achat non atteint
- BTC-EUR : 68013 € ; score 79.84/100 ; SURVEILLE ; seuil achat non atteint
- XPL-EUR : 0.078043 € ; score 78.98/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.68498 € ; score 77.01/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 92.383 € ; score 76.84/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.00665 | +80.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014893 | +41.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.45989 | +35.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.154957 | +28.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.7068 | +25.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18231 | +25.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.030725 | +25.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.009 | +25.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.21908 | +19.05 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.51069 | +18.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 784 scans ; 336514 observations ; 154 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
