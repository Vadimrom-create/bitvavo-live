# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-15T18:24:40.161079+00:00
État : OK | marchés EUR : 429 | V4 : 370 | données valides : 5
Récupération : 2026-09-15T18:24:12.096165+00:00 | âge ticker : 137.0 s | durée : 137.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/429 ; 15 min 67/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- UNI-EUR : 5.5718 € ; score 89.06/100 ; SURVEILLE ; seuil achat non atteint
- VTHO-EUR : 0.00064187 € ; score 80.84/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, VERTICAL_SHORT_TERM
- USELESS-EUR : 0.181225 € ; score 79.19/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.35517 € ; score 77.28/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ALIGN-EUR | 0.006867 | +38.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.02041 | +33.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PUFFER-EUR | 0.020054 | +19.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.29277 | +16.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ASTR-EUR | 0.0060561 | +14.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NES-EUR | 0.13897 | +14.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LAPTOP-EUR | 0.20596 | +10.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.00064187 | +9.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CROSS-EUR | 0.108873 | +9.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| GLMR-EUR | 0.00508 | +8.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 570 scans ; 244556 observations ; 98 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
