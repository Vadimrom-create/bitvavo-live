# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T19:10:15.441963+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T19:09:37.737593+00:00 | âge ticker : 162.5 s | durée : 163.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- XAI-EUR : 0.0081941 € ; score 90.59/100 ; SURVEILLE ; seuil achat non atteint
- SNX-EUR : 0.2255 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- JASMY-EUR : 0.0046625 € ; score 86.80/100 ; SURVEILLE ; WICK_SETUP
- UNI-EUR : 7.9697 € ; score 86.77/100 ; SURVEILLE ; WICK_SETUP
- RARE-EUR : 0.015449 € ; score 86.40/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016698 | +32.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.29406 | +25.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35922 | +24.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDP-EUR | 0.021132 | +22.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZBCN-EUR | 0.0021377 | +21.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 1.0238 | +20.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.59632 | +17.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 11.4454 | +16.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.091226 | +15.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 235.65 | +14.29 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1787 scans ; 764533 observations ; 1338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
