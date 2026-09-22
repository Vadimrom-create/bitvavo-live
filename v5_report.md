# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T23:45:30.459552+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T23:45:02.512661+00:00 | âge ticker : 143.1 s | durée : 143.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- APT-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- EIGEN-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XPL-EUR : 0.084115 € | IGNITION | score 84.36/100 | entrée 6.75/10
  Entrée 0.084051 € ; stop 0.080952 € ; TP1 0.090249 € ; TP2 0.093348 € ; montant 250.00 € ; risque théorique 10.94 € ; R/R net 1.52.
  Chase risk : 3.45/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FIL-EUR : 0.91461 € ; score 92.14/100 ; SURVEILLE ; WICK_SETUP
- CHZ-EUR : 0.014971 € ; score 89.58/100 ; SURVEILLE ; seuil achat non atteint
- PROVE-EUR : 0.19884 € ; score 88.67/100 ; SURVEILLE ; SPREAD_RISK
- CHIP-EUR : 0.040616 € ; score 87.85/100 ; SURVEILLE ; seuil achat non atteint
- TRUMP-EUR : 1.959 € ; score 86.42/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.02045 | +36.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 301.82 | +29.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.053656 | +29.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.019635 | +26.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.303202 | +24.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.071261 | +18.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.075734 | +18.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2057 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BTT-EUR | 3.3499e-07 | +16.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12092 | +16.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1226 scans ; 525013 observations ; 562 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
