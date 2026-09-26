# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T12:11:31.645843+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T12:11:00.613596+00:00 | âge ticker : 147.2 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 291.31 € | IGNITION | score 92.50/100 | entrée 7.15/10
  Entrée 291.04 € ; stop 273.47 € ; TP1 326.18 € ; TP2 343.75 € ; montant 178.68 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 6.358/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.81453 € | IGNITION | score 87.62/100 | entrée 7.10/10
  Entrée 1.8153 € ; stop 1.72964 € ; TP1 1.98661 € ; TP2 2.07227 € ; montant 222.13 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.5/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVAX-EUR : 9.5815 € ; score 92.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.42871 € ; score 87.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.4513 € ; score 87.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOL-EUR : 106.459 € ; score 87.33/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : 1.0395 € ; score 87.21/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020526 | +156.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020104 | +70.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006502 | +45.82 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062378 | +27.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.07115 | +24.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24392 | +21.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PROM-EUR | 5.7396 | +20.18 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AERO-EUR | 0.81113 | +17.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24764 | +17.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WAXP-EUR | 0.0060452 | +12.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1530 scans ; 654678 observations ; 984 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
