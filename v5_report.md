# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T08:44:34.407169+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 10
Récupération : 2026-09-18T08:44:04.490112+00:00 | âge ticker : 138.3 s | durée : 139.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/430 ; 15 min 68/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_15M, STALE_DAILY_PROFILE
- PEPE-EUR : STALE_DAILY_PROFILE
- SYRUP-EUR : INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00059 € ; score 87.74/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SUI-EUR : 0.68107 € ; score 79.99/100 ; SURVEILLE ; seuil achat non atteint
- BTC-EUR : 67861 € ; score 76.25/100 ; SURVEILLE ; STABILITY_HOLD
- XRP-EUR : 1.16077 € ; score 74.91/100 ; SURVEILLE ; seuil achat non atteint
- AKT-EUR : 0.47674 € ; score 74.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0072752 | +97.57 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014823 | +41.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.46196 | +34.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.15472 | +28.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.006 | +26.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UNI-EUR | 7.69 | +26.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.030435 | +24.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18092 | +24.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.22414 | +21.55 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.004967 | +17.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 783 scans ; 336084 observations ; 154 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
