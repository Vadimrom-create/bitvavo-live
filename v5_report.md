# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T20:18:37.740035+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T20:18:08.085464+00:00 | âge ticker : 164.2 s | durée : 165.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.41732 € | IGNITION | score 90.19/100 | entrée 7.45/10
  Entrée 0.41745 € ; stop 0.40021 € ; TP1 0.45192 € ; TP2 0.46916 € ; montant 249.20 € ; risque théorique 12.00 € ; R/R net 1.56.
  Chase risk : 4.475/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SENT-EUR : 0.020461 € | IGNITION | score 80.09/100 | entrée 6.55/10
  Entrée 0.020524 € ; stop 0.01972 € ; TP1 0.022132 € ; TP2 0.022935 € ; montant 250.00 € ; risque théorique 11.51 € ; R/R net 1.54.
  Chase risk : 4.549/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ORCA-EUR : 1.45121 € ; score 92.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.0055475 € ; score 91.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.68844 € ; score 91.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALICE-EUR : 0.13952 € ; score 90.95/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- STX-EUR : 0.28784 € ; score 90.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.072724 | +65.19 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21208 | +28.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.0143 | +24.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WMTX-EUR | 0.022486 | +21.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.088752 | +19.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.065 | +19.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.46142 | +17.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22988 | +17.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.72176 | +17.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LDO-EUR | 0.44037 | +14.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1469 scans ; 628631 observations ; 882 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
