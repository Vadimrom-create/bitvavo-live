# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T07:12:28.604580+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 9
Récupération : 2026-09-18T07:12:00.438014+00:00 | âge ticker : 139.0 s | durée : 139.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/430 ; 15 min 65/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LINK-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- XLM-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 212.5 € ; score 84.35/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.15398 € ; score 82.31/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 117.11 € ; score 80.79/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0052785 | +43.35 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014606 | +40.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18671 | +28.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.43291 | +28.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0338 | +27.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CROSS-EUR | 0.151915 | +27.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.019726 | +27.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.5233 | +26.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.21729 | +19.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.0049 | +18.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 777 scans ; 333504 observations ; 152 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
