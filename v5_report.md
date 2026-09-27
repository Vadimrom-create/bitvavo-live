# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T07:37:07.088262+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T07:36:37.642684+00:00 | âge ticker : 154.1 s | durée : 155.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AVAX-EUR : 9.8207 € | IGNITION | score 86.94/100 | entrée 7.60/10
  Entrée 9.8096 € ; stop 9.4323 € ; TP1 10.5642 € ; TP2 10.9415 € ; montant 250.00 € ; risque théorique 11.33 € ; R/R net 1.54.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RED-EUR : 0.15186 € ; score 93.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TIA-EUR : 0.43894 € ; score 92.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MANA-EUR : 0.08151 € ; score 92.25/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- TREE-EUR : 0.043325 € ; score 91.64/100 ; SURVEILLE ; SPREAD_RISK
- MOVR-EUR : 0.9112 € ; score 91.43/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 149.058 | +70.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.009248 | +57.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.26299 | +39.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006001 | +33.33 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00644 | +26.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.121046 | +21.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013073 | +18.81 % | DETECTED_EARLY | NONE | NONE |
| HFT-EUR | 0.006401 | +16.83 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PYTH-EUR | 0.07607 | +16.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.69786 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1598 scans ; 683714 observations ; 1096 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
