# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T16:22:46.042534+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T16:22:02.999518+00:00 | âge ticker : 159.2 s | durée : 159.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- F-EUR : 0.0032528 € ; score 87.34/100 ; SURVEILLE ; seuil achat non atteint
- ZORA-EUR : 0.007404 € ; score 87.13/100 ; SURVEILLE ; seuil achat non atteint
- HMSTR-EUR : 0.00015418 € ; score 85.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.03713 € ; score 85.36/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.254 € ; score 84.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0027251 | +250.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.021986 | +160.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053652 | +61.47 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.043805 | +37.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30678 | +37.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008504 | +31.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.100069 | +29.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.056951 | +28.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.31998 | +26.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0009556 | +25.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1089 scans ; 466651 observations ; 391 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
