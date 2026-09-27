# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T12:00:12.210666+00:00
État : OK | marchés EUR : 427 | V4 : 379 | données valides : 427
Récupération : 2026-09-27T11:59:35.365333+00:00 | âge ticker : 159.4 s | durée : 160.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PENGU-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TRUST-EUR : 0.058687 € ; score 93.03/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.026716 € ; score 92.17/100 ; SURVEILLE ; seuil achat non atteint
- PENGU-EUR : 0.00903 € ; score 89.35/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EUL-EUR : 1.3179 € ; score 88.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ENA-EUR : 0.24212 € ; score 87.56/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GLMR-EUR | 0.009067 | +56.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 143.568 | +56.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.1116 | +55.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.24396 | +28.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.124045 | +24.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006265 | +20.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.006583 | +19.13 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WLD-EUR | 0.50896 | +18.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.54539 | +18.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006213 | +17.31 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1614 scans ; 690546 observations ; 1130 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
