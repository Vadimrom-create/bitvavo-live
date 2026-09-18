# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T13:00:17.460171+00:00
État : OK | marchés EUR : 427 | V4 : 371 | données valides : 10
Récupération : 2026-09-18T12:59:47.636238+00:00 | âge ticker : 143.7 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 39/427 ; 15 min 81/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- RENDER-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- W-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.40714 € ; score 89.81/100 ; SURVEILLE ; SPREAD_RISK
- VET-EUR : 0.0065824 € ; score 80.79/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.34439 € ; score 78.68/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0070501 | +85.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.4731 | +40.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.1851 | +30.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.013592 | +27.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.1322 | +25.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UNI-EUR | 7.516 | +25.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.029396 | +21.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6036 | +21.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.027508 | +19.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.49185 | +18.76 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 798 scans ; 342525 observations ; 161 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
