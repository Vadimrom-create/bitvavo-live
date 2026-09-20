# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T02:04:32.007660+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 22
Récupération : 2026-09-20T02:04:02.792845+00:00 | âge ticker : 152.2 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/427 ; 15 min 61/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- OP-EUR : INVALID_15M, INVALID_5M
- POL-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- UNI-EUR : CHASE_RISK, INVALID_5M
- VET-EUR : CHASE_RISK, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- FET-EUR : 0.1551 € ; score 75.10/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 95.976 € ; score 74.23/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SUI-EUR : 0.75272 € ; score 72.89/100 ; SURVEILLE ; WICK_SETUP
- ALGO-EUR : 0.093528 € ; score 72.18/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0039274 | +96.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0102971 | +64.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZAMA-EUR | 0.072285 | +29.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.18956 | +25.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.9958 | +18.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.0040671 | +17.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOLV-EUR | 0.0040276 | +17.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.28822 | +16.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0031397 | +15.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.065345 | +15.70 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 942 scans ; 404013 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
