# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T18:43:30.163094+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T18:42:57.669909+00:00 | âge ticker : 155.5 s | durée : 157.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.18834 € ; score 91.65/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.21313 € ; score 88.95/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.03659 € ; score 88.30/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.058227 € ; score 86.50/100 ; SURVEILLE ; seuil achat non atteint
- SPX-EUR : 0.46674 € ; score 85.39/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.022232 | +50.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.021418 | +40.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 296.01 | +28.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.072119 | +27.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050559 | +21.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12098 | +17.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2069 | +16.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GOAT-EUR | 0.018642 | +16.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.37473 | +15.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.47 | +15.74 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1205 scans ; 516067 observations ; 533 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
