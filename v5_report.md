# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T02:29:26.576615+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T02:28:56.898998+00:00 | âge ticker : 142.2 s | durée : 143.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.5792 € | IGNITION | score 83.90/100 | entrée 7.25/10
  Entrée 9.5688 € ; stop 9.2303 € ; TP1 10.2458 € ; TP2 10.5842 € ; montant 250.00 € ; risque théorique 10.56 € ; R/R net 1.50.
  Chase risk : 3.713/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- EIGEN-EUR : 0.22776 € ; score 93.83/100 ; SURVEILLE ; seuil achat non atteint
- PROM-EUR : 5.3163 € ; score 92.11/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.22979 € ; score 91.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WOO-EUR : 0.011831 € ; score 90.24/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KAS-EUR : 0.037264 € ; score 89.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.078813 | +78.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0012514 | +60.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.22436 | +36.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.102086 | +30.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.77381 | +26.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23511 | +18.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065568 | +17.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013224 | +16.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.11813 | +16.56 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.021555 | +16.31 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1495 scans ; 639733 observations ; 923 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
