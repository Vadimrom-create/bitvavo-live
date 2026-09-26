# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T21:02:53.568121+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-26T21:02:19.360584+00:00 | âge ticker : 156.5 s | durée : 157.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- EIGEN-EUR : 0.23564 € ; score 83.92/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.975 € ; score 83.33/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BLUR-EUR : 0.01815 € ; score 82.54/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.102788 € ; score 82.38/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7212 € ; score 82.01/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016659 | +106.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0007107 | +60.21 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.12331 | +42.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.01886 | +37.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 105.973 | +23.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.043795 | +20.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061481 | +18.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.006062 | +18.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.65961 | +17.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KAS-EUR | 0.042328 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1562 scans ; 668342 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
