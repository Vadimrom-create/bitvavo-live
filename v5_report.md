# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T19:43:49.993748+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T19:43:21.808617+00:00 | âge ticker : 143.2 s | durée : 143.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- VVV-EUR : 27.9162 € | IGNITION | score 89.29/100 | entrée 6.85/10
  Entrée 27.8 € ; stop 26.3367 € ; TP1 30.7266 € ; TP2 32.1899 € ; montant 201.84 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 5.571/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAO-EUR : 261.7 € ; score 91.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EDEN-EUR : 0.05543 € ; score 90.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HUMA-EUR : 0.022676 € ; score 88.99/100 ; SURVEILLE ; SPREAD_RISK
- GMT-EUR : 0.007677 € ; score 88.95/100 ; SURVEILLE ; WICK_SETUP
- WOO-EUR : 0.011231 € ; score 88.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0099532 | +44.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38327 | +35.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.001985 | +25.24 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ONDO-EUR | 0.45281 | +24.93 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.58512 | +24.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 75.551 | +21.18 % | DETECTED_EARLY | NONE | NONE |
| PLUME-EUR | 0.0163321 | +20.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.093512 | +19.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.036708 | +18.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10189 | +18.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1381 scans ; 591055 observations ; 757 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
