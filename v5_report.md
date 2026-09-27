# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T05:56:14.909917+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T05:55:49.597827+00:00 | âge ticker : 139.6 s | durée : 140.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.7174 € | IGNITION | score 87.38/100 | entrée 7.40/10
  Entrée 4.7222 € ; stop 4.3697 € ; TP1 5.4272 € ; TP2 5.7797 € ; montant 147.45 € ; risque théorique 12.00 € ; R/R net 1.74.
  Chase risk : 3.84/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ENA-EUR : 0.23857 € ; score 93.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SPK-EUR : 0.0216 € ; score 92.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AKT-EUR : 0.61658 € ; score 92.17/100 ; SURVEILLE ; seuil achat non atteint
- XPL-EUR : 0.098472 € ; score 90.91/100 ; SURVEILLE ; WICK_SETUP
- PLUME-EUR : 0.0159629 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 154.22 | +73.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26275 | +43.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019137 | +40.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006241 | +39.28 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006502 | +26.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007248 | +25.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.70518 | +21.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.012671 | +17.02 % | DETECTED_EARLY | NONE | NONE |
| PYTH-EUR | 0.074671 | +16.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1593 scans ; 681579 observations ; 1092 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
