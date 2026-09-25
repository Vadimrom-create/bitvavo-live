# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T15:21:52.418893+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T15:21:14.517587+00:00 | âge ticker : 163.4 s | durée : 164.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.28843 € | IGNITION | score 84.14/100 | entrée 7.30/10
  Entrée 0.28821 € ; stop 0.27508 € ; TP1 0.31447 € ; TP2 0.3276 € ; montant 229.02 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.416/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LDO-EUR : 0.40003 € | IGNITION | score 81.62/100 | entrée 6.55/10
  Entrée 0.40092 € ; stop 0.38399 € ; TP1 0.43478 € ; TP2 0.45171 € ; montant 244.50 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.234/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PYTH-EUR : 0.06461 € ; score 90.10/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.4404 € ; score 84.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PIXEL-EUR : 0.0053047 € ; score 83.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZK-EUR : 0.011225 € ; score 82.43/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- MANTRA-EUR : 0.004208 € ; score 82.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.067773 | +55.21 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.71359 | +44.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19719 | +26.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 0.9881 | +23.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.087537 | +21.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 83.964 | +19.20 % | DETECTED_EARLY | NONE | NONE |
| KMNO-EUR | 0.038024 | +18.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.4448 | +17.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.11693 | +17.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.22234 | +17.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1452 scans ; 621372 observations ; 865 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
