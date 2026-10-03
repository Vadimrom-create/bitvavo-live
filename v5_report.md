# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T10:16:08.916538+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-10-03T10:15:41.241927+00:00 | âge ticker : 150.7 s | durée : 151.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.52333 € | IGNITION | score 93.99/100 | entrée 7.25/10
  Entrée 0.52387 € ; stop 0.49272 € ; TP1 0.58616 € ; TP2 0.61731 € ; montant 181.12 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 6.336/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.19982 € | IGNITION | score 87.43/100 | entrée 7.65/10
  Entrée 0.20046 € ; stop 0.19293 € ; TP1 0.21552 € ; TP2 0.22305 € ; montant 250.00 € ; risque théorique 11.11 € ; R/R net 1.53.
  Chase risk : 3.764/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PUMP-EUR : 0.0049333 € ; score 90.19/100 ; SURVEILLE ; WICK_SETUP
- MEGA-EUR : 0.04188 € ; score 89.05/100 ; SURVEILLE ; WICK_SETUP
- RENDER-EUR : 1.7424 € ; score 88.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DEEP-EUR : 0.021351 € ; score 87.39/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- TIA-EUR : 0.40827 € ; score 87.37/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.06749 | +22.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.006535 | +15.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ATH-EUR | 0.0062827 | +14.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008868 | +12.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.22605 | +12.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 229.189 | +11.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.06406 | +11.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.52333 | +9.12 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.66741 | +8.66 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.006222 | +8.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 2043 scans ; 874304 observations ; 1608 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
