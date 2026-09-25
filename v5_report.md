# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T18:19:18.907603+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-25T18:18:44.494730+00:00 | âge ticker : 152.6 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.29039 € | IGNITION | score 90.21/100 | entrée 7.55/10
  Entrée 0.29039 € ; stop 0.27944 € ; TP1 0.31228 € ; TP2 0.32323 € ; montant 250.00 € ; risque théorique 11.14 € ; R/R net 1.53.
  Chase risk : 2.879/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XAI-EUR : 0.008192 € | IGNITION | score 84.80/100 | entrée 6.35/10
  Entrée 0.0082201 € ; stop 0.0078693 € ; TP1 0.0089217 € ; TP2 0.0092725 € ; montant 242.29 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.472/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- OP-EUR : 0.12251 € ; score 92.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.7771 € ; score 88.09/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0082876 € ; score 86.69/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.032882 € ; score 85.83/100 ; SURVEILLE ; WICK_SETUP
- AXS-EUR : 1.0406 € ; score 85.66/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| WMTX-EUR | 0.025694 | +78.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.071979 | +66.28 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.207 | +29.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.48158 | +26.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.75555 | +22.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014167 | +22.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.087836 | +21.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.22932 | +20.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.67298 | +19.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.062102 | +16.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1462 scans ; 625642 observations ; 878 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
