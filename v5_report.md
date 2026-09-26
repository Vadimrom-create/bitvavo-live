# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T16:43:35.105738+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T16:43:03.893437+00:00 | âge ticker : 152.6 s | durée : 153.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.1264 € | IGNITION | score 84.83/100 | entrée 7.20/10
  Entrée 1.1268 € ; stop 1.078 € ; TP1 1.2244 € ; TP2 1.2731 € ; montant 239.25 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.057/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XLM-EUR : 0.19364 € ; score 93.11/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GOAT-EUR : 0.017919 € ; score 92.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ARPA-EUR : 0.010308 € ; score 91.46/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- MERL-EUR : 0.025974 € ; score 91.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- TREE-EUR : 0.0435 € ; score 90.37/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018 | +123.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.000616 | +38.15 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019035 | +35.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.112416 | +29.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 106.387 | +24.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006218 | +22.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ACE-EUR | 0.20381 | +21.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 1.06744 | +18.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.66769 | +18.51 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| 2Z-EUR | 0.060423 | +18.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1546 scans ; 661510 observations ; 1013 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
