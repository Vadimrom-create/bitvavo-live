# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T23:31:41.118243+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T23:30:47.856187+00:00 | âge ticker : 169.6 s | durée : 170.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AVAX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XPL-EUR : 0.084707 € | IGNITION | score 87.46/100 | entrée 7.20/10
  Entrée 0.084751 € ; stop 0.080994 € ; TP1 0.092265 € ; TP2 0.096022 € ; montant 234.49 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.738/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ICP-EUR : 2.6329 € ; score 92.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.9159 € ; score 92.14/100 ; SURVEILLE ; WICK_SETUP
- CHZ-EUR : 0.014971 € ; score 90.36/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.024059 € ; score 89.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAT-EUR : 0.004459 € ; score 89.32/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019973 | +33.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.053867 | +29.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 299.54 | +27.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019497 | +25.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.307605 | +25.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2316 | +20.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.07634 | +19.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.070537 | +17.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.3499e-07 | +16.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12092 | +16.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1225 scans ; 524587 observations ; 561 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
