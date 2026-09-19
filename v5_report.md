# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T23:32:40.002565+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 28
Récupération : 2026-09-19T23:32:07.227364+00:00 | âge ticker : 156.4 s | durée : 157.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/427 ; 15 min 75/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : INVALID_5M
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- NPC-EUR : INVALID_5M
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- VET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- HYPE-EUR : 79.852 € ; score 80.99/100 ; SURVEILLE ; WICK_SETUP
- PEPE-EUR : 3.5959e-06 € ; score 79.61/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.74872 € ; score 78.18/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.36583 € ; score 76.79/100 ; SURVEILLE ; WICK_SETUP
- NEAR-EUR : 3.1272 € ; score 76.56/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0029058 | +45.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.072292 | +40.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0090457 | +35.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.074963 | +26.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.31972 | +25.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.9895 | +21.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.6692 | +21.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENA-EUR | 0.1783 | +21.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.004015 | +16.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024595 | +13.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 933 scans ; 400170 observations ; 222 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
