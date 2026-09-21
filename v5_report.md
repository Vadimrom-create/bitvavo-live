# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T18:22:06.634635+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-21T18:21:33.531547+00:00 | âge ticker : 153.6 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NEO-EUR : 2.166 € ; score 89.73/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0047842 € ; score 87.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZORA-EUR : 0.007361 € ; score 87.16/100 ; SURVEILLE ; seuil achat non atteint
- ETC-EUR : 7.7609 € ; score 86.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- CHR-EUR : 0.015236 € ; score 85.46/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0021029 | +171.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017 | +101.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.05271 | +56.63 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31676 | +41.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043394 | +36.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.098716 | +25.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.000816 | +25.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3385e-06 | +24.76 % | DETECTED_EARLY | NONE | NONE |
| PTB-EUR | 0.0010011 | +23.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.22622 | +22.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1099 scans ; 470911 observations ; 401 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
