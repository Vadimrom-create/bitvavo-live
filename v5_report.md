# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T22:38:06.743127+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T22:37:36.470162+00:00 | âge ticker : 149.0 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 64.497 € | IGNITION | score 88.15/100 | entrée 7.20/10
  Entrée 64.554 € ; stop 61.847 € ; TP1 69.968 € ; TP2 72.675 € ; montant 245.97 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.848/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PENGU-EUR : 0.009054 € | IGNITION | score 75.18/100 | entrée 7.20/10
  Entrée 0.0090542 € ; stop 0.0086984 € ; TP1 0.0097658 € ; TP2 0.0101216 € ; montant 250.00 € ; risque théorique 11.54 € ; R/R net 1.55.
  Chase risk : 2.968/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DOGE-EUR : 0.087131 € ; score 90.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AEVO-EUR : 0.022999 € ; score 89.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ORCA-EUR : 1.4521 € ; score 89.23/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.2007 € ; score 89.10/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- S-EUR : 0.03615 € ; score 89.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.081551 | +83.25 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RARE-EUR | 0.014247 | +25.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.2122 | +24.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.74008 | +22.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065156 | +20.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23352 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.02046 | +18.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SUI-EUR | 1.04307 | +17.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.087634 | +16.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.45185 | +16.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1479 scans ; 632901 observations ; 896 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
