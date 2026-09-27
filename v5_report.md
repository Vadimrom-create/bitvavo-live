# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T06:59:36.102990+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T06:59:10.548576+00:00 | âge ticker : 142.5 s | durée : 143.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : 289.26 € | IGNITION | score 93.06/100 | entrée 7.35/10
  Entrée 289.55 € ; stop 278.53 € ; TP1 311.59 € ; TP2 322.61 € ; montant 250.00 € ; risque théorique 11.23 € ; R/R net 1.53.
  Chase risk : 2.202/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 8.8082 € | IGNITION | score 85.82/100 | entrée 7.20/10
  Entrée 8.8165 € ; stop 8.4888 € ; TP1 9.4719 € ; TP2 9.7996 € ; montant 250.00 € ; risque théorique 11.01 € ; R/R net 1.52.
  Chase risk : 4.97/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.1165 € | IGNITION | score 79.76/100 | entrée 6.50/10
  Entrée 1.1144 € ; stop 1.074 € ; TP1 1.1952 € ; TP2 1.2356 € ; montant 40.78 € ; risque théorique 1.76 € ; R/R net 1.51.
  Chase risk : 3.924/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZK-EUR : 0.011625 € ; score 93.35/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ONDO-EUR : 0.47403 € ; score 93.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.032404 € ; score 92.77/100 ; SURVEILLE ; seuil achat non atteint
- MOVR-EUR : 0.8993 € ; score 92.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PIXEL-EUR : 0.0053465 € ; score 92.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 148.964 | +67.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26051 | +37.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006136 | +35.96 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007806 | +32.33 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| HFT-EUR | 0.006887 | +25.70 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006403 | +25.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.122577 | +22.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.69459 | +17.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.012826 | +17.59 % | DETECTED_EARLY | NONE | NONE |
| PYTH-EUR | 0.074693 | +15.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1596 scans ; 682860 observations ; 1094 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
