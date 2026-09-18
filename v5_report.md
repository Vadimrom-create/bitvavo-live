# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T04:52:47.264342+00:00
État : OK | marchés EUR : 430 | V4 : 364 | données valides : 8
Récupération : 2026-09-18T04:52:16.422738+00:00 | âge ticker : 144.7 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/430 ; 15 min 47/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- RENDER-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 210.4 € ; score 85.68/100 ; SURVEILLE ; WICK_SETUP
- LSK-EUR : 0.40154 € ; score 82.09/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SYRUP-EUR : 0.18324 € ; score 80.68/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0036372 € ; score 78.09/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.16407 € ; score 70.61/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.23117 | +50.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.013809 | +33.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020373 | +31.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19129 | +31.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0742 | +31.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.43624 | +28.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.53673 | +27.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.4707 | +25.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00512 | +24.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CROSS-EUR | 0.148543 | +24.10 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 768 scans ; 329634 observations ; 144 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
