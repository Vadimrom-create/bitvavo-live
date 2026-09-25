# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T22:50:53.435009+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T22:50:24.906973+00:00 | âge ticker : 145.6 s | durée : 146.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PENGU-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.70032 € | IGNITION | score 88.44/100 | entrée 7.65/10
  Entrée 0.7009 € ; stop 0.67587 € ; TP1 0.75096 € ; TP2 0.77599 € ; montant 250.00 € ; risque théorique 10.65 € ; R/R net 1.51.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LTC-EUR : 64.119 € | IGNITION | score 84.91/100 | entrée 7.40/10
  Entrée 64.159 € ; stop 61.829 € ; TP1 68.819 € ; TP2 71.149 € ; montant 250.00 € ; risque théorique 10.80 € ; R/R net 1.51.
  Chase risk : 4.261/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ARB-EUR : 0.20126 € | IGNITION | score 83.65/100 | entrée 6.55/10
  Entrée 0.20172 € ; stop 0.19214 € ; TP1 0.22088 € ; TP2 0.23046 € ; montant 47.05 € ; risque théorique 2.56 € ; R/R net 1.61.
  Chase risk : 2.986/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ADA-EUR : 0.22694 € ; score 92.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.85274 € ; score 92.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2039 € ; score 91.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KSM-EUR : 4.1781 € ; score 87.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DOGE-EUR : 0.087213 € ; score 86.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.080371 | +80.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.22827 | +32.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013972 | +22.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.73162 | +21.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065268 | +20.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23509 | +19.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.02046 | +18.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SUI-EUR | 1.04 | +17.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.45991 | +17.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JTO-EUR | 0.49997 | +15.60 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1480 scans ; 633328 observations ; 897 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
