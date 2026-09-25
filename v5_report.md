# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T23:48:05.793090+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-25T23:47:30.698006+00:00 | âge ticker : 156.8 s | durée : 158.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.100838 € | IGNITION | score 89.19/100 | entrée 7.40/10
  Entrée 0.100912 € ; stop 0.096339 € ; TP1 0.110058 € ; TP2 0.114631 € ; montant 230.07 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 2.68/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZK-EUR : 0.01135 € ; score 93.22/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ENS-EUR : 6.3056 € ; score 90.53/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7061 € ; score 90.24/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.102197 € ; score 88.11/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AEVO-EUR : 0.023184 € ; score 87.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.072959 | +62.94 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0011542 | +47.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.22428 | +31.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014144 | +23.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74645 | +21.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065526 | +19.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23467 | +19.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 1.05507 | +18.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022513 | +18.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.45611 | +18.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1485 scans ; 635463 observations ; 902 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
