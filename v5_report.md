# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T04:58:13.036853+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T04:57:45.603267+00:00 | âge ticker : 143.3 s | durée : 144.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.008572 € | IGNITION | score 92.57/100 | entrée 7.40/10
  Entrée 0.0085666 € ; stop 0.0082619 € ; TP1 0.009176 € ; TP2 0.0094807 € ; montant 250.00 € ; risque théorique 10.61 € ; R/R net 1.51.
  Chase risk : 2.083/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- KAS-EUR : 0.038324 € | IGNITION | score 91.93/100 | entrée 7.25/10
  Entrée 0.038441 € ; stop 0.036961 € ; TP1 0.041401 € ; TP2 0.042881 € ; montant 250.00 € ; risque théorique 11.34 € ; R/R net 1.54.
  Chase risk : 3.744/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DOT-EUR : 1.0757 € ; score 93.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CHR-EUR : 0.019 € ; score 91.10/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- RENDER-EUR : 1.6996 € ; score 89.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HNT-EUR : 0.44797 € ; score 88.88/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- ALGO-EUR : 0.102316 € ; score 88.15/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001601 | +106.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.074427 | +68.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.22518 | +31.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78144 | +26.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24514 | +25.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.033747 | +22.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.064954 | +18.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013287 | +16.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037544 | +16.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JTO-EUR | 0.50696 | +16.55 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1504 scans ; 643576 observations ; 946 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
