# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T20:40:52.506587+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T20:40:22.324259+00:00 | âge ticker : 156.3 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZIG-EUR : 0.04542 € ; score 88.45/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.27923 € ; score 87.76/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SAND-EUR : 0.035256 € ; score 87.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BCH-EUR : 218.68 € ; score 87.52/100 ; SURVEILLE ; seuil achat non atteint
- COW-EUR : 0.1357 € ; score 86.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032149 | +49.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.25987 | +41.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.00079 | +29.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.035648 | +25.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.054656 | +24.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6556 | +18.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028048 | +17.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.042897 | +17.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8109 | +16.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELR-EUR | 0.0030306 | +16.24 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1015 scans ; 435127 observations ; 264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
