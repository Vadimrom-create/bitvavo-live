# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T05:08:27.252561+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 9
Récupération : 2026-09-18T05:07:55.507778+00:00 | âge ticker : 138.7 s | durée : 139.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/430 ; 15 min 48/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- USELESS-EUR : 0.23585 € ; score 77.60/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 211.49 € ; score 76.63/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- SYRUP-EUR : 0.1836 € ; score 75.66/100 ; SURVEILLE ; STABILITY_HOLD
- XRP-EUR : 1.14945 € ; score 75.11/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.2248 | +39.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.0572 | +31.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COTI-EUR | 0.020003 | +29.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.42992 | +29.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.013266 | +27.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.5456 | +26.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.151413 | +25.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.3404 | +23.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18506 | +23.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.005003 | +21.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 769 scans ; 330064 observations ; 144 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
