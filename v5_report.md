# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T18:24:01.276027+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T18:23:23.924101+00:00 | âge ticker : 154.0 s | durée : 154.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LDO-EUR : 0.37087 € ; score 86.90/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.40228 € ; score 85.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.20856 € ; score 84.25/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ATOM-EUR : 1.5614 € ; score 83.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SSV-EUR : 2.8909 € ; score 83.00/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.021544 | +45.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.021276 | +39.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.072029 | +29.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 296.15 | +28.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050617 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.37898 | +18.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12149 | +18.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2137 | +18.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.285298 | +15.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.038477 | +14.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1204 scans ; 515641 observations ; 533 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
