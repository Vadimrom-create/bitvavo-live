# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T01:02:53.657045+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T01:02:21.953148+00:00 | âge ticker : 149.2 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FIL-EUR : 0.86605 € ; score 87.86/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.0234 € ; score 87.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IOST-EUR : 0.0007933 € ; score 87.50/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- RSR-EUR : 0.0014369 € ; score 87.07/100 ; SURVEILLE ; seuil achat non atteint
- SSV-EUR : 2.9033 € ; score 85.70/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01912 | +126.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014748 | +88.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.120381 | +49.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.050116 | +45.46 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.044996 | +36.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30664 | +34.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008832 | +33.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010682 | +30.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3184e-06 | +22.24 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21263 | +19.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1136 scans ; 486673 observations ; 435 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
