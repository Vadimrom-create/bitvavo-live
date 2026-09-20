# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T02:23:41.955811+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 22
Récupération : 2026-09-20T02:23:12.674996+00:00 | âge ticker : 150.2 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/427 ; 15 min 59/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- OP-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- PENDLE-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- VET-EUR : INVALID_5M

## SURVEILLE

- SOL-EUR : 95.71 € ; score 72.86/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- LINK-EUR : 10.7099 € ; score 72.28/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0041677 | +106.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0104829 | +58.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZAMA-EUR | 0.071996 | +30.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0033915 | +25.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.18627 | +22.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOLV-EUR | 0.0040715 | +18.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.9956 | +17.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.142 | +16.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.28792 | +16.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKL-EUR | 0.0039917 | +15.34 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 943 scans ; 404440 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
