# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T15:36:19.196542+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-26T15:35:52.497462+00:00 | âge ticker : 148.7 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, PORTFOLIO_LIMIT
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, PORTFOLIO_LIMIT
- ICP-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.43744 € | IGNITION | score 94.41/100 | entrée 7.45/10
  Entrée 0.43779 € ; stop 0.42076 € ; TP1 0.47185 € ; TP2 0.48888 € ; montant 250.00 € ; risque théorique 11.44 € ; R/R net 1.54.
  Chase risk : 2.504/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VIRTUAL-EUR : 0.71111 € | IGNITION | score 91.88/100 | entrée 7.30/10
  Entrée 0.71303 € ; stop 0.6826 € ; TP1 0.77389 € ; TP2 0.80432 € ; montant 242.29 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.299/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AVAX-EUR : 9.7574 € | IGNITION | score 88.62/100 | entrée 7.40/10
  Entrée 9.7596 € ; stop 9.3704 € ; TP1 10.538 € ; TP2 10.9272 € ; montant 11.96 € ; risque théorique 0.56 € ; R/R net 1.55.
  Chase risk : 3.194/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WAL-EUR : 0.033292 € ; score 94.23/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.22845 € ; score 94.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AIXBT-EUR : 0.022093 € ; score 93.50/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- ZK-EUR : 0.011475 € ; score 93.46/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- STX-EUR : 0.30261 € ; score 92.48/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017743 | +109.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020164 | +34.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.114073 | +30.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005674 | +28.37 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062943 | +25.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 103.421 | +24.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HUMA-EUR | 0.026865 | +20.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.044962 | +19.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FIL-EUR | 1.06072 | +19.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.66505 | +18.30 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1542 scans ; 659802 observations ; 1008 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
