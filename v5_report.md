# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T23:46:30.967989+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 26
Récupération : 2026-09-19T23:45:58.582277+00:00 | âge ticker : 146.4 s | durée : 147.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/427 ; 15 min 72/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- NPC-EUR : SPREAD_RISK, STABILITY_HOLD, INVALID_5M
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- STX-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- HYPE-EUR : 79.773 € ; score 80.36/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.75076 € ; score 77.78/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.5819e-06 € ; score 77.55/100 ; SURVEILLE ; STABILITY_HOLD
- ONDO-EUR : 0.36502 € ; score 77.25/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 96.548 € ; score 77.21/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0028682 | +43.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.009207 | +39.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.071247 | +38.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.074963 | +26.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.32124 | +24.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.81 | +23.64 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENA-EUR | 0.1779 | +21.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.8476 | +18.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.003965 | +14.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.025825 | +13.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 934 scans ; 400597 observations ; 222 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
