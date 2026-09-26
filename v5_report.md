# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T20:35:03.060113+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T20:34:29.552226+00:00 | âge ticker : 151.5 s | durée : 152.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- STRK-EUR : 0.036153 € ; score 88.09/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0056377 € ; score 84.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AEVO-EUR : 0.024287 € ; score 83.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ICNT-EUR : 0.0888 € ; score 83.77/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.201 € ; score 83.43/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017001 | +107.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0007181 | +61.88 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.124675 | +43.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019653 | +37.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 105.96 | +23.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006232 | +21.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.044055 | +20.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LAPTOP-EUR | 0.07646 | +18.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.06138 | +18.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.66095 | +17.15 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1560 scans ; 667488 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
