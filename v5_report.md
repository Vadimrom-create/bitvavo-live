# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T10:07:19.163675+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T10:06:48.312555+00:00 | âge ticker : 148.6 s | durée : 149.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETC-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FIL-EUR : 0.90278 € ; score 92.32/100 ; SURVEILLE ; seuil achat non atteint
- SPK-EUR : 0.019385 € ; score 90.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KITE-EUR : 0.11913 € ; score 89.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LUNA-EUR : 4.9342e-05 € ; score 87.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ARK-EUR : 0.14117 € ; score 87.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.03555 | +42.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 318.3 | +35.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.3333 | +32.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019546 | +28.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.291163 | +27.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16633 | +25.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.285 | +24.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.46918 | +23.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0096743 | +22.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.083427 | +19.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1261 scans ; 539923 observations ; 637 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
