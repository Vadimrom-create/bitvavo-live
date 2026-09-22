# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T04:41:27.499497+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T04:40:59.577280+00:00 | âge ticker : 143.3 s | durée : 144.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DRIFT-EUR : 0.015657 € | IGNITION | score 91.89/100 | entrée 7.45/10
  Entrée 0.015753 € ; stop 0.015073 € ; TP1 0.017113 € ; TP2 0.017793 € ; montant 239.93 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.048/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- YGG-EUR : 0.02292 € ; score 88.63/100 ; SURVEILLE ; seuil achat non atteint
- NPC-EUR : 0.02 € ; score 85.91/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- PLUME-EUR : 0.0129534 € ; score 83.21/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- MERL-EUR : 0.02419 € ; score 82.96/100 ; SURVEILLE ; seuil achat non atteint
- MANTA-EUR : 0.061685 € ; score 82.62/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.023432 | +171.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013748 | +76.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.056972 | +47.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.116171 | +46.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.046726 | +37.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5752e-06 | +30.75 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.22104 | +24.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27999 | +22.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CARV-EUR | 0.041029 | +21.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FARTCOIN-EUR | 0.18 | +19.28 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1149 scans ; 492211 observations ; 455 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
