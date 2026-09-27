# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T18:38:36.652237+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T18:38:05.785878+00:00 | âge ticker : 155.4 s | durée : 156.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.24901 € | IGNITION | score 93.19/100 | entrée 7.90/10
  Entrée 0.24807 € ; stop 0.23876 € ; TP1 0.26669 € ; TP2 0.276 € ; montant 250.00 € ; risque théorique 11.10 € ; R/R net 1.53.
  Chase risk : 5.035/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- CC-EUR : 0.12149 € | IGNITION | score 84.60/100 | entrée 6.80/10
  Entrée 0.12156 € ; stop 0.11677 € ; TP1 0.13114 € ; TP2 0.13593 € ; montant 250.00 € ; risque théorique 11.57 € ; R/R net 1.55.
  Chase risk : 4.256/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.04283 € ; score 94.57/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 287.21 € ; score 93.73/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZK-EUR : 0.0118 € ; score 93.57/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- CRO-EUR : 0.059278 € ; score 92.79/100 ; SURVEILLE ; SPREAD_RISK
- ALGO-EUR : 0.104901 € ; score 92.55/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 164.547 | +55.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28564 | +47.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.02109 | +37.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016211 | +27.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006537 | +26.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.24412 | +19.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.00712 | +18.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.013498 | +17.20 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.006984 | +16.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.017499 | +15.23 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1637 scans ; 700367 observations ; 1164 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
