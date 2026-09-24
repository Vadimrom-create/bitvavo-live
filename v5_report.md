# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T06:59:34.943694+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-24T06:59:05.888644+00:00 | âge ticker : 143.3 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.0146956 € ; score 93.56/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- MAVIA-EUR : 0.029576 € ; score 85.56/100 ; SURVEILLE ; WICK_SETUP
- DEEP-EUR : 0.016718 € ; score 85.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- INIT-EUR : 0.0802 € ; score 84.28/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- FIL-EUR : 0.86828 € ; score 82.99/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0023133 | +50.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.33894 | +23.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.11347 | +23.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELR-EUR | 0.00303 | +17.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.85839 | +16.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019336 | +13.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.018526 | +10.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28859 | +10.24 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.3811 | +9.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BOME-EUR | 0.00107241 | +8.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1336 scans ; 571873 observations ; 687 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
