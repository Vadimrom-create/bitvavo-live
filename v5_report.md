# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T06:57:52.858371+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 6
Récupération : 2026-09-18T06:57:21.962646+00:00 | âge ticker : 140.3 s | durée : 141.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/430 ; 15 min 58/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LINK-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- W-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 211.89 € ; score 84.26/100 ; SURVEILLE ; WICK_SETUP
- LSK-EUR : 0.39189 € ; score 78.04/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0058517 | +58.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014257 | +37.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0258 | +29.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.43571 | +28.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18643 | +28.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.0198 | +28.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.4958 | +27.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.150379 | +25.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.2185 | +20.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.004966 | +20.65 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 776 scans ; 333074 observations ; 152 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
