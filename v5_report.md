# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T04:00:26.244753+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-10-01T03:59:53.731312+00:00 | âge ticker : 161.4 s | durée : 163.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.11492 € | IGNITION | score 86.83/100 | entrée 6.80/10
  Entrée 0.115026 € ; stop 0.109348 € ; TP1 0.126382 € ; TP2 0.13206 € ; montant 213.56 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.485/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.1156 € ; score 93.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DEEP-EUR : 0.020666 € ; score 92.00/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- MMT-EUR : 0.16652 € ; score 91.65/100 ; SURVEILLE ; STABILITY_HOLD
- DYDX-EUR : 0.13 € ; score 91.58/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- IMX-EUR : 0.1527 € ; score 91.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.117 | +88.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35251 | +47.49 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.00929 | +37.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.42654 | +25.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028985 | +23.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.3434 | +23.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PLUME-EUR | 0.018352 | +17.55 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.46646 | +14.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KAIA-EUR | 0.033938 | +13.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.4107 | +13.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1884 scans ; 806198 observations ; 1438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
