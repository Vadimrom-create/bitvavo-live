# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T16:06:46.278306+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T16:06:18.540800+00:00 | âge ticker : 147.4 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.1244 € | IGNITION | score 92.77/100 | entrée 7.80/10
  Entrée 1.1254 € ; stop 1.0702 € ; TP1 1.2357 € ; TP2 1.2909 € ; montant 214.76 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.567/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ALGO-EUR : 0.1074 € | IGNITION | score 84.81/100 | entrée 7.10/10
  Entrée 0.106913 € ; stop 0.102444 € ; TP1 0.115851 € ; TP2 0.12032 € ; montant 246.64 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.505/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XLM-EUR : 0.19319 € ; score 93.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.083498 € ; score 92.75/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HOT-EUR : 0.00040066 € ; score 92.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- REZ-EUR : 0.0039597 € ; score 92.48/100 ; SURVEILLE ; seuil achat non atteint
- SAND-EUR : 0.040626 € ; score 91.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017265 | +112.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019286 | +37.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0005918 | +33.89 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.1148 | +32.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HUMA-EUR | 0.027325 | +22.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061724 | +21.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 101.224 | +21.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47864 | +19.25 % | DETECTED_EARLY | NONE | NONE |
| ACE-EUR | 0.19925 | +19.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.66815 | +18.94 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1544 scans ; 660656 observations ; 1012 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
