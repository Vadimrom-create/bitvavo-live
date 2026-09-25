# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T08:26:13.869320+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T08:25:49.192179+00:00 | âge ticker : 140.0 s | durée : 140.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : 0.65116 € | IGNITION | score 94.23/100 | entrée 7.25/10
  Entrée 0.65232 € ; stop 0.62769 € ; TP1 0.70158 € ; TP2 0.72621 € ; montant 250.00 € ; risque théorique 11.16 € ; R/R net 1.53.
  Chase risk : 5.741/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 4.0942 € | IGNITION | score 86.77/100 | entrée 7.00/10
  Entrée 4.0909 € ; stop 3.8994 € ; TP1 4.4739 € ; TP2 4.6654 € ; montant 223.68 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 2.314/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ICP-EUR : 2.7991 € | IGNITION | score 80.76/100 | entrée 6.90/10
  Entrée 2.7982 € ; stop 2.6869 € ; TP1 3.0208 € ; TP2 3.1321 € ; montant 18.09 € ; risque théorique 0.84 € ; R/R net 1.55.
  Chase risk : 2.928/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.6512 € ; score 92.92/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.9025 € ; score 91.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.2188e-06 € ; score 91.31/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.008183 € ; score 91.05/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GRASS-EUR : 0.42218 € ; score 91.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.72192 | +45.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 89.059 | +42.26 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.50649 | +33.29 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.103437 | +30.45 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.18697 | +23.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.049195 | +21.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.0865 | +19.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LDO-EUR | 0.41159 | +19.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DBR-EUR | 0.021554 | +18.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0081715 | +17.16 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1430 scans ; 611978 observations ; 818 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
