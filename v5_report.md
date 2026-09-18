# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T10:55:50.104066+00:00
État : OK | marchés EUR : 430 | V4 : 373 | données valides : 8
Récupération : 2026-09-18T10:55:20.704601+00:00 | âge ticker : 142.3 s | durée : 143.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/430 ; 15 min 75/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INVALID_5M, STALE_DAILY_PROFILE
- KAS-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- PHA-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XLM-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00060772 € ; score 84.92/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.258e-06 € ; score 82.37/100 ; SURVEILLE ; seuil achat non atteint
- USDC-EUR : 0.8716 € ; score 81.09/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.3912 € ; score 76.96/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.07505 € ; score 72.44/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0063796 | +74.01 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.46733 | +37.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.7856 | +31.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.50867 | +30.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.013704 | +29.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0839 | +26.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00529 | +25.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.18007 | +25.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.051 | +24.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.029643 | +21.90 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 791 scans ; 339524 observations ; 157 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
