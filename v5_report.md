# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-13T14:46:29.749603+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 6
Récupération : 2026-09-13T14:46:01.744894+00:00 | âge ticker : 135.6 s | durée : 136.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/429 ; 15 min 60/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- NPC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- SUI-EUR : INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- XLM-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 203.64 € ; score 85.81/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 109.52 € ; score 80.29/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.30091 € ; score 77.59/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 86.924 € ; score 77.34/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.7619 | +232.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.034723 | +82.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PUNDIX-EUR | 0.11549 | +30.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.13082 | +26.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRAX-EUR | 0.010636 | +20.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| GLM-EUR | 0.11503 | +19.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.00069772 | +17.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POWR-EUR | 0.053479 | +15.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.033602 | +13.74 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| BAT-EUR | 0.07082 | +12.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 399 scans ; 171197 observations ; 57 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
