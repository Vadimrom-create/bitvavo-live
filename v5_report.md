# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T10:27:19.715391+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T10:26:15.826343+00:00 | âge ticker : 182.9 s | durée : 183.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZEN-EUR : 7.1095 € ; score 91.98/100 ; SURVEILLE ; SPREAD_RISK
- CHIP-EUR : 0.040215 € ; score 90.26/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- KITE-EUR : 0.11913 € ; score 85.61/100 ; SURVEILLE ; seuil achat non atteint
- CHZ-EUR : 0.014839 € ; score 83.74/100 ; SURVEILLE ; seuil achat non atteint
- AUCTION-EUR : 3.44 € ; score 81.74/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034612 | +38.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.297816 | +31.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.33 | +31.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 307.82 | +31.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019666 | +30.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.16544 | +25.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2734 | +24.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.46347 | +23.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0093848 | +21.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.019676 | +20.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1262 scans ; 540349 observations ; 637 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
