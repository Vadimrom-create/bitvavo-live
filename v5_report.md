# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T17:33:26.932617+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T17:32:28.913129+00:00 | âge ticker : 176.4 s | durée : 177.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ESP-EUR : 0.09283 € ; score 89.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PROMPT-EUR : 0.020056 € ; score 88.40/100 ; SURVEILLE ; seuil achat non atteint
- ID-EUR : 0.03519 € ; score 87.40/100 ; SURVEILLE ; LOW_LIQUIDITY
- GRAM-EUR : 1.3393 € ; score 86.93/100 ; SURVEILLE ; seuil achat non atteint
- ZIL-EUR : 0.0033914 € ; score 85.85/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016335 | +106.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.126421 | +45.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.000624 | +39.94 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.01996 | +39.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 107.764 | +25.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061553 | +20.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.042843 | +18.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47478 | +18.30 % | DETECTED_EARLY | NONE | NONE |
| KMNO-EUR | 0.043727 | +18.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005982 | +17.41 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1549 scans ; 662791 observations ; 1014 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
