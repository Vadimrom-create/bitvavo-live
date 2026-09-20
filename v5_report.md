# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T02:40:38.120588+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 25
Récupération : 2026-09-20T02:40:08.212969+00:00 | âge ticker : 155.7 s | durée : 156.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/427 ; 15 min 57/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PENDLE-EUR : SPREAD_RISK, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- VET-EUR : STABILITY_HOLD, INVALID_5M

## SURVEILLE

- SOL-EUR : 95.186 € ; score 75.27/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 79.356 € ; score 75.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0040915 | +103.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0103613 | +55.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZAMA-EUR | 0.071228 | +32.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0032492 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGLD-EUR | 0.19057 | +18.45 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOLV-EUR | 0.0040535 | +17.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17797 | +16.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.939 | +16.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.0039923 | +15.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.140046 | +14.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 944 scans ; 404867 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
