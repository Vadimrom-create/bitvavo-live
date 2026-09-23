# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T09:52:06.908484+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T09:51:34.940804+00:00 | âge ticker : 145.4 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- MOVR-EUR : 0.8342 € ; score 90.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KAT-EUR : 0.004523 € ; score 87.97/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- XAI-EUR : 0.0072831 € ; score 86.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- TREAD-EUR : 0.49999 € ; score 84.85/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- AAVE-EUR : 131.29 € ; score 84.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.036123 | +47.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.33871 | +34.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 313.29 | +33.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.17284 | +30.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019373 | +27.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.288468 | +25.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2721 | +23.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.47077 | +22.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0096575 | +21.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.085249 | +20.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1260 scans ; 539497 observations ; 635 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
