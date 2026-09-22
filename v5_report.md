# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T20:20:26.082950+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T20:19:53.792487+00:00 | âge ticker : 152.4 s | durée : 154.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETC-EUR : 8.0525 € ; score 90.28/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COMP-EUR : 19.903 € ; score 89.12/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0051904 € ; score 88.01/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- XAI-EUR : 0.0071634 € ; score 83.19/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.3094 € ; score 82.34/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020961 | +41.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020422 | +31.64 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 296.8 | +27.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051463 | +24.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069647 | +20.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.292804 | +17.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12157 | +17.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GOAT-EUR | 0.018504 | +15.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.008941 | +14.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.48993 | +14.47 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1213 scans ; 519475 observations ; 534 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
