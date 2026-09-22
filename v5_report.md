# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T17:58:35.657489+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T17:58:08.400304+00:00 | âge ticker : 142.0 s | durée : 142.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- MEGA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CHZ-EUR : 0.01475 € ; score 90.45/100 ; SURVEILLE ; WICK_SETUP
- CHIP-EUR : 0.040443 € ; score 90.14/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- SSV-EUR : 2.8849 € ; score 89.64/100 ; SURVEILLE ; WICK_SETUP
- ZBT-EUR : 0.07792 € ; score 87.69/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- METIS-EUR : 3.144 € ; score 87.54/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.021665 | +43.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.072253 | +32.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 292.04 | +27.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.018549 | +25.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050558 | +24.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2357 | +21.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.37847 | +18.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.076332 | +17.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.11982 | +16.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.027148 | +15.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1203 scans ; 515215 observations ; 529 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
