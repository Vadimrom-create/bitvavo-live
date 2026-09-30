# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T14:53:37.813349+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 429
Récupération : 2026-09-30T14:52:32.298274+00:00 | âge ticker : 253.4 s | durée : 254.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- HUMA-EUR : 0.027698 € ; score 86.37/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- SENT-EUR : 0.019426 € ; score 83.10/100 ; SURVEILLE ; WICK_SETUP
- BLUR-EUR : 0.019098 € ; score 80.91/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- INIT-EUR : 0.092301 € ; score 79.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- DYDX-EUR : 0.12837 € ; score 79.09/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.48329 | +58.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.4385 | +56.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.33025 | +38.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ARK-EUR | 0.27531 | +26.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021818 | +21.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 255.402 | +17.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.082036 | +16.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.48401 | +12.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GLMR-EUR | 0.007514 | +12.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.086092 | +11.44 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1845 scans ; 789428 observations ; 1388 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
