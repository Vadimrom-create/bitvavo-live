# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T08:26:21.703460+00:00
État : OK | marchés EUR : 430 | V4 : 364 | données valides : 8
Récupération : 2026-09-18T08:25:51.252303+00:00 | âge ticker : 143.0 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 33/430 ; 15 min 67/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_15M, STALE_DAILY_PROFILE
- PEPE-EUR : STALE_DAILY_PROFILE
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- AKT-EUR : 0.47734 € ; score 85.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- VTHO-EUR : 0.00059434 € ; score 85.01/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- BTC-EUR : 67916 € ; score 80.70/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.16237 € ; score 79.62/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.3365 € ; score 78.68/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0066161 | +79.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014845 | +41.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.47726 | +38.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.155014 | +29.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.6694 | +27.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0007 | +25.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.17996 | +25.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.03028 | +24.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.22581 | +22.46 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| COTI-EUR | 0.018991 | +18.76 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 782 scans ; 335654 observations ; 153 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
