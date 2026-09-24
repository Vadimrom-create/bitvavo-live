# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T14:45:34.330462+00:00
État : OK | marchés EUR : 426 | V4 : 390 | données valides : 426
Récupération : 2026-09-24T14:45:04.857039+00:00 | âge ticker : 151.5 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : BELOW_EXCHANGE_MINIMUM
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOGE-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- FLOKI-EUR : BELOW_EXCHANGE_MINIMUM
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : BELOW_EXCHANGE_MINIMUM
- PYTH-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : BELOW_EXCHANGE_MINIMUM
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : BELOW_EXCHANGE_MINIMUM
- W-EUR : BELOW_EXCHANGE_MINIMUM
- ADA-EUR : 0.21851 € | IGNITION | score 92.27/100 | entrée 8.05/10
  Entrée 0.21843 € ; stop 0.20636 € ; TP1 0.24257 € ; TP2 0.25464 € ; montant 193.35 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 6.484/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- HBAR-EUR : 0.083035 € | IGNITION | score 92.15/100 | entrée 7.60/10
  Entrée 0.083016 € ; stop 0.078926 € ; TP1 0.091196 € ; TP2 0.095286 € ; montant 213.92 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.968/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ARPA-EUR : 0.0099264 € ; score 91.92/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- UNI-EUR : 8.1173 € ; score 91.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.9355e-06 € ; score 91.69/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- KAS-EUR : 0.034973 € ; score 91.30/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.097781 € ; score 91.14/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0020509 | +36.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.34791 | +29.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.101482 | +26.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.44554 | +21.67 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 64.4 | +20.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.21948 | +15.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.03513 | +15.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.015763 | +14.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19564 | +13.28 % | DETECTED_EARLY | NONE | NONE |
| ETC-EUR | 8.8535 | +13.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1362 scans ; 582949 observations ; 717 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
