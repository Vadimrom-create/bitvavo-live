# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T21:27:22.151049+00:00
État : OK | marchés EUR : 426 | V4 : 380 | données valides : 426
Récupération : 2026-09-20T21:26:48.522980+00:00 | âge ticker : 148.6 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CAKE-EUR : 2.241 € ; score 89.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- MOODENG-EUR : 0.038589 € ; score 86.31/100 ; SURVEILLE ; STABILITY_HOLD
- STX-EUR : 0.28283 € ; score 86.01/100 ; SURVEILLE ; seuil achat non atteint
- GAS-EUR : 1.1705 € ; score 84.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRIA-EUR : 0.003422 € ; score 83.41/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032773 | +50.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008068 | +32.92 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.24404 | +32.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.05393 | +23.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.003063 | +22.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49056 | +19.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.034097 | +19.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6024 | +16.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027915 | +16.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.047863 | +15.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1018 scans ; 436405 observations ; 272 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
