# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T09:22:03.492241+00:00
État : OK | marchés EUR : 426 | V4 : 379 | données valides : 426
Récupération : 2026-09-21T09:21:34.121346+00:00 | âge ticker : 151.8 s | durée : 153.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : BELOW_EXCHANGE_MINIMUM
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : BELOW_EXCHANGE_MINIMUM
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.18055 € | IGNITION | score 88.73/100 | entrée 7.80/10
  Entrée 0.18065 € ; stop 0.17219 € ; TP1 0.19757 € ; TP2 0.20603 € ; montant 223.60 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 5.344/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PEPE-EUR : 3.6245e-06 € | IGNITION | score 88.27/100 | entrée 7.40/10
  Entrée 3.626e-06 € ; stop 3.4653e-06 € ; TP1 3.9474e-06 € ; TP2 4.1081e-06 € ; montant 234.54 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.978/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DOT-EUR : 1.0291 € ; score 92.38/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUSHI-EUR : 0.22452 € ; score 89.64/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 11.1943 € ; score 89.16/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : 0.37866 € ; score 87.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.097106 € ; score 87.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.058 | +74.67 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.000986 | +60.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.058514 | +34.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.03239 | +33.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.030373 | +29.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23679 | +29.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PHA-EUR | 0.04 | +28.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031337 | +26.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.51892 | +24.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 0.87377 | +22.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1063 scans ; 455575 observations ; 336 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
