# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T16:01:23.740055+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-21T16:00:49.139677+00:00 | âge ticker : 161.5 s | durée : 162.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CAKE-EUR : 2.256 € ; score 89.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- CC-EUR : 0.10165 € ; score 87.41/100 ; SURVEILLE ; WICK_SETUP
- CHZ-EUR : 0.013931 € ; score 87.16/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.037005 € ; score 86.48/100 ; SURVEILLE ; seuil achat non atteint
- HMSTR-EUR : 0.00015418 € ; score 85.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0027266 | +250.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.052448 | +58.26 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.043652 | +36.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.100972 | +32.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.056628 | +29.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.4392e-06 | +29.16 % | DETECTED_EARLY | NONE | NONE |
| PTB-EUR | 0.00095 | +28.40 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.030886 | +23.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21505 | +23.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.051206 | +22.43 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1088 scans ; 466225 observations ; 387 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
