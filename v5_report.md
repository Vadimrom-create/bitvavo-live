# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T18:43:37.694016+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-26T18:43:06.287810+00:00 | âge ticker : 149.7 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SPK-EUR : 0.022424 € ; score 93.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ETC-EUR : 8.3221 € ; score 91.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0038812 € ; score 89.82/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0083239 € ; score 89.16/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.2637 € ; score 88.69/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018994 | +135.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006458 | +44.83 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.126 | +40.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019907 | +38.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 105.717 | +22.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.043909 | +22.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061287 | +19.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.043407 | +18.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005988 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.4702 | +16.13 % | DETECTED_EARLY | NONE | NONE |

Historique : 1553 scans ; 664499 observations ; 1022 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
