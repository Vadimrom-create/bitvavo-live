# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T18:18:28.228739+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T18:17:56.590309+00:00 | âge ticker : 149.7 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FIL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.1206 € | IGNITION | score 85.82/100 | entrée 7.05/10
  Entrée 0.12069 € ; stop 0.11587 € ; TP1 0.13033 € ; TP2 0.13515 € ; montant 250.00 € ; risque théorique 11.70 € ; R/R net 1.55.
  Chase risk : 3.133/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 4.6717 € | IGNITION | score 83.17/100 | entrée 7.75/10
  Entrée 4.6737 € ; stop 4.4971 € ; TP1 5.0269 € ; TP2 5.2035 € ; montant 250.00 € ; risque théorique 11.16 € ; R/R net 1.53.
  Chase risk : 2.835/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ENA-EUR : 0.24799 € | IGNITION | score 81.62/100 | entrée 7.25/10
  Entrée 0.2482 € ; stop 0.23878 € ; TP1 0.26704 € ; TP2 0.27646 € ; montant 25.37 € ; risque théorique 1.14 € ; R/R net 1.53.
  Chase risk : 4.899/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- APT-EUR : 0.75 € ; score 92.75/100 ; SURVEILLE ; seuil achat non atteint
- FIDA-EUR : 0.02 € ; score 90.89/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ONDO-EUR : 0.48703 € ; score 90.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEAQ-EUR : 0.038034 € ; score 89.87/100 ; SURVEILLE ; STABILITY_HOLD
- DOT-EUR : 1.1046 € ; score 88.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.28928 | +50.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 162.61 | +49.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 1.03999 | +40.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016039 | +26.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006521 | +25.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.24813 | +21.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.007102 | +18.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007026 | +17.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.013365 | +16.24 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.004462 | +13.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1636 scans ; 699940 observations ; 1164 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
