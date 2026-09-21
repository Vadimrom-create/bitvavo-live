# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T12:07:17.176138+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-09-21T12:06:44.113416+00:00 | âge ticker : 157.1 s | durée : 158.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.21739 € | IGNITION | score 87.60/100 | entrée 7.50/10
  Entrée 0.21744 € ; stop 0.20824 € ; TP1 0.23583 € ; TP2 0.24503 € ; montant 244.09 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.514/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAO-EUR : 247.5 € | IGNITION | score 80.69/100 | entrée 7.60/10
  Entrée 247.56 € ; stop 238.79 € ; TP1 265.1 € ; TP2 273.87 € ; montant 250.00 € ; risque théorique 10.58 € ; R/R net 1.50.
  Chase risk : 4.015/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.39473 € | IGNITION | score 78.32/100 | entrée 7.80/10
  Entrée 0.39508 € ; stop 0.37675 € ; TP1 0.43174 € ; TP2 0.45007 € ; montant 26.76 € ; risque théorique 1.42 € ; R/R net 1.61.
  Chase risk : 3.363/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAIKO-EUR : 0.07963 € ; score 91.80/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.20552 € ; score 88.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.029883 € ; score 88.29/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023907 € ; score 87.39/100 ; SURVEILLE ; WICK_SETUP
- KAITO-EUR : 0.30226 € ; score 84.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.058497 | +74.78 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.053112 | +67.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009864 | +38.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.031349 | +31.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.055857 | +29.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.05247 | +26.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23108 | +26.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.031892 | +24.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.887 | +23.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.091625 | +21.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1074 scans ; 460261 observations ; 354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
