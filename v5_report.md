# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T23:56:20.690946+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-25T23:55:49.039437+00:00 | âge ticker : 149.2 s | durée : 150.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.22322 € | IGNITION | score 89.25/100 | entrée 7.50/10
  Entrée 0.22364 € ; stop 0.21244 € ; TP1 0.24604 € ; TP2 0.25724 € ; montant 210.88 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 1.833/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XPL-EUR : 0.100637 € | IGNITION | score 89.01/100 | entrée 6.85/10
  Entrée 0.10068 € ; stop 0.096339 € ; TP1 0.109362 € ; TP2 0.113703 € ; montant 240.16 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 2.68/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CHIP-EUR : 0.044439 € ; score 91.62/100 ; SURVEILLE ; WICK_SETUP
- ENS-EUR : 6.3056 € ; score 90.53/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.949e-06 € ; score 90.17/100 ; SURVEILLE ; WICK_SETUP
- PENDLE-EUR : 2.239 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ZK-EUR : 0.011306 € ; score 87.29/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.074849 | +67.35 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.00129 | +65.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.22371 | +30.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014169 | +24.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74765 | +21.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065362 | +19.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23547 | +18.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022543 | +18.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.45611 | +18.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.71953 | +18.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1486 scans ; 635890 observations ; 904 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
