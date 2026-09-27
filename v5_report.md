# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T06:42:13.440324+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T06:41:46.592015+00:00 | âge ticker : 146.5 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : 8.9456 € | IGNITION | score 91.96/100 | entrée 7.40/10
  Entrée 8.9263 € ; stop 8.4979 € ; TP1 9.7831 € ; TP2 10.2115 € ; montant 218.88 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 1.677/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VET-EUR : 0.0082362 € | IGNITION | score 90.48/100 | entrée 6.80/10
  Entrée 0.0082463 € ; stop 0.0079334 € ; TP1 0.008872 € ; TP2 0.0091849 € ; montant 250.00 € ; risque théorique 11.20 € ; R/R net 1.53.
  Chase risk : 0.737/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZK-EUR : 0.011624 € ; score 93.35/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- TAO-EUR : 287.27 € ; score 92.47/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PIXEL-EUR : 0.0053465 € ; score 92.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- APT-EUR : 0.7566 € ; score 92.09/100 ; SURVEILLE ; WICK_SETUP
- DOT-EUR : 1.0996 € ; score 91.97/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 157.131 | +73.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006137 | +36.96 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008059 | +36.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.25162 | +35.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006866 | +25.31 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006184 | +20.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.012946 | +19.13 % | DETECTED_EARLY | NONE | NONE |
| EDGE-EUR | 0.1184 | +17.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.68775 | +17.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0012303 | +17.20 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1595 scans ; 682433 observations ; 1093 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
