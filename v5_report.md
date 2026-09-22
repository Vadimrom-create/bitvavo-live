# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T23:15:46.319727+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T23:15:20.099633+00:00 | âge ticker : 149.9 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.072 € | IGNITION | score 91.42/100 | entrée 7.15/10
  Entrée 1.0718 € ; stop 1.034 € ; TP1 1.1474 € ; TP2 1.1852 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 4.485/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.036393 € ; score 92.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MANA-EUR : 0.077862 € ; score 91.07/100 ; SURVEILLE ; seuil achat non atteint
- GMT-EUR : 0.007638 € ; score 90.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CHZ-EUR : 0.01494 € ; score 90.45/100 ; SURVEILLE ; WICK_SETUP
- TURBO-EUR : 0.0009673 € ; score 89.61/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020363 | +35.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.054114 | +28.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 299.92 | +26.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019379 | +24.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.306675 | +24.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.076552 | +19.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2124 | +18.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069969 | +17.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12218 | +17.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0088569 | +15.81 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1224 scans ; 524161 observations ; 556 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
