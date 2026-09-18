# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T11:14:29.269026+00:00
État : OK | marchés EUR : 430 | V4 : 372 | données valides : 9
Récupération : 2026-09-18T11:14:01.816451+00:00 | âge ticker : 140.3 s | durée : 141.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/430 ; 15 min 74/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NPC-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- PHA-EUR : SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.00365 € ; score 84.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VTHO-EUR : 0.0005965 € ; score 81.87/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.14892 € ; score 81.71/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.074114 € ; score 65.42/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0071178 | +94.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.472 | +39.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.567 | +26.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.50754 | +25.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.01316 | +24.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.17989 | +23.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0181 | +23.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005166 | +22.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.029595 | +21.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 5.7523 | +18.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 792 scans ; 339954 observations ; 157 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
