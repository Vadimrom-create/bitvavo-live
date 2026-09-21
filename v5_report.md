# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T20:49:45.437554+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T20:49:16.191101+00:00 | âge ticker : 144.6 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : LOW_LIQUIDITY, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.29883 € | IGNITION | score 87.61/100 | entrée 7.15/10
  Entrée 0.30063 € ; stop 0.28581 € ; TP1 0.33027 € ; TP2 0.34509 € ; montant 213.81 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.227/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.39735 € | IGNITION | score 84.66/100 | entrée 7.40/10
  Entrée 0.39782 € ; stop 0.3754 € ; TP1 0.44266 € ; TP2 0.46508 € ; montant 189.99 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 6.267/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.010302 € ; score 93.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.38 € ; score 90.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MEME-EUR : 0.0005235 € ; score 88.69/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.097743 € ; score 88.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : 1.33415 € ; score 86.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0185 | +119.56 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0016996 | +117.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.052645 | +52.80 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.1119 | +41.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31374 | +39.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.001082 | +36.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.04368 | +33.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008002 | +23.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.257516 | +22.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.26e-06 | +22.17 % | DETECTED_EARLY | NONE | NONE |

Historique : 1114 scans ; 477301 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
