# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T06:01:02.668430+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T06:00:31.846323+00:00 | âge ticker : 160.0 s | durée : 160.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : SPREAD_RISK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0039638 € | IGNITION | score 83.59/100 | entrée 7.40/10
  Entrée 0.003959 € ; stop 0.0038197 € ; TP1 0.0042375 € ; TP2 0.0043768 € ; montant 250.00 € ; risque théorique 10.52 € ; R/R net 1.50.
  Chase risk : 3.012/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MOVR-EUR : 0.7705 € ; score 90.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SENT-EUR : 0.016987 € ; score 88.77/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- CHIP-EUR : 0.041006 € ; score 88.46/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 101.902 € ; score 88.16/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SSV-EUR : 2.871 € ; score 85.75/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015022 | +93.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0158 | +82.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.122224 | +54.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057246 | +33.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.504e-06 | +28.62 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.38525 | +22.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27479 | +21.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAO-EUR | 281.95 | +20.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.036673 | +20.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WIF-EUR | 0.21306 | +19.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1154 scans ; 494341 observations ; 463 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
