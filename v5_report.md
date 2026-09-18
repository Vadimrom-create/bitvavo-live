# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T18:12:58.340179+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 5
Récupération : 2026-09-18T18:12:26.744354+00:00 | âge ticker : 147.8 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 44/427 ; 15 min 88/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- PHA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 217.4 € ; score 76.03/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0037604 € ; score 73.31/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0072706 | +84.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.52264 | +46.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0040125 | +44.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.03329 | +33.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.062143 | +27.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.3172 | +25.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.02175 | +22.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19406 | +21.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6061 | +20.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| A-EUR | 0.080458 | +20.04 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 817 scans ; 350638 observations ; 176 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
