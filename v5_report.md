# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T08:00:16.715079+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T07:59:47.057764+00:00 | âge ticker : 154.0 s | durée : 155.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- API3-EUR : 0.24414 € ; score 93.15/100 ; SURVEILLE ; WICK_SETUP
- ARPA-EUR : 0.0100018 € ; score 90.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AI-EUR : 0.018587 € ; score 88.41/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- CRV-EUR : 0.31564 € ; score 86.11/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.030667 € ; score 85.43/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.096109 | +48.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.033692 | +37.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31978 | +34.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 305.58 | +30.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.16862 | +28.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019107 | +23.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| UP-EUR | 0.064599 | +20.66 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.2456 | +20.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020087 | +19.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0094627 | +19.14 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1254 scans ; 536941 observations ; 620 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
