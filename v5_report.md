# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T21:10:38.707382+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T21:10:05.234835+00:00 | âge ticker : 153.1 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MIOTA-EUR : 0.041247 € ; score 89.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- GALA-EUR : 0.0016735 € ; score 87.74/100 ; SURVEILLE ; STABILITY_HOLD
- WAXP-EUR : 0.0045527 € ; score 86.30/100 ; SURVEILLE ; SPREAD_RISK
- CAKE-EUR : 2.2467 € ; score 84.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- BTC-EUR : 70369 € ; score 84.41/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032772 | +50.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.2457 | +34.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.000792 | +30.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CELR-EUR | 0.0030523 | +23.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.053378 | +20.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.033924 | +18.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.02798 | +16.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.5959 | +16.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.48765 | +16.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.047699 | +15.89 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1017 scans ; 435979 observations ; 269 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
