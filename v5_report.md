# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T05:48:51.927728+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T05:48:20.357560+00:00 | âge ticker : 147.7 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0085969 € | IGNITION | score 92.57/100 | entrée 7.50/10
  Entrée 0.0085893 € ; stop 0.008258 € ; TP1 0.0092518 € ; TP2 0.0095831 € ; montant 250.00 € ; risque théorique 11.36 € ; R/R net 1.54.
  Chase risk : 3.258/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- S-EUR : 0.036075 € ; score 91.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CRO-EUR : 0.057815 € ; score 87.71/100 ; SURVEILLE ; SPREAD_RISK
- ARPA-EUR : 0.0100716 € ; score 87.14/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- AI-EUR : 0.018791 € ; score 86.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NPC-EUR : 0.0196893 € ; score 86.33/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001606 | +105.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.0765 | +63.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.2378 | +35.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022823 | +26.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.78633 | +24.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23942 | +22.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.102648 | +18.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.013363 | +16.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037568 | +16.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.033337 | +15.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1507 scans ; 644857 observations ; 951 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
