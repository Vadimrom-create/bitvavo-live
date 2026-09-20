# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T01:20:38.932993+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 21
Récupération : 2026-09-20T01:20:07.098604+00:00 | âge ticker : 144.8 s | durée : 145.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/427 ; 15 min 66/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_15M, INVALID_5M
- HBAR-EUR : WICK_SETUP, INVALID_5M
- POL-EUR : STABILITY_HOLD, INVALID_5M
- RENDER-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- SYRUP-EUR : WICK_SETUP, INVALID_5M
- TAO-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- TAO-EUR : 231.38 € ; score 89.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.5404e-06 € ; score 77.84/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 96.106 € ; score 73.59/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0036181 | +81.40 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.009593 | +53.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.070279 | +28.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.1827 | +23.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.074699 | +20.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 8.6737 | +20.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZIL-EUR | 0.0032595 | +20.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKL-EUR | 0.0041575 | +19.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 7.0465 | +19.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XTZ-EUR | 0.29946 | +17.76 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 939 scans ; 402732 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
