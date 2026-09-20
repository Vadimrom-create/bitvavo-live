# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T18:01:52.216977+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 46
Récupération : 2026-09-20T18:00:53.162336+00:00 | âge ticker : 182.8 s | durée : 184.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 49/426 ; 15 min 83/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- JUP-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- OP-EUR : CHASE_RISK, INVALID_15M, INVALID_5M

## SURVEILLE

- ENSO-EUR : 0.8801 € ; score 79.72/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.027965 € ; score 78.64/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.526 € ; score 78.63/100 ; SURVEILLE ; seuil achat non atteint
- DOT-EUR : 1.0032 € ; score 75.58/100 ; SURVEILLE ; STABILITY_HOLD
- PLUME-EUR : 0.012166 € ; score 75.16/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0031901 | +47.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.030219 | +36.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008359 | +35.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23007 | +25.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.074288 | +21.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.049248 | +17.89 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.5837 | +14.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.049295 | +13.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.031823 | +13.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.21402 | +12.77 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1003 scans ; 430015 observations ; 236 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
