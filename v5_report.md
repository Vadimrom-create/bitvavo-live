# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T20:56:36.237161+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T20:56:09.515174+00:00 | âge ticker : 143.4 s | durée : 144.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : LOW_LIQUIDITY, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.30318 € | IGNITION | score 89.57/100 | entrée 6.75/10
  Entrée 0.30298 € ; stop 0.28581 € ; TP1 0.33732 € ; TP2 0.35449 € ; montant 189.06 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 5.227/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.40346 € | IGNITION | score 73.20/100 | entrée 7.15/10
  Entrée 0.40372 € ; stop 0.3754 € ; TP1 0.46036 € ; TP2 0.48868 € ; montant 156.04 € ; risque théorique 12.00 € ; R/R net 1.73.
  Chase risk : 6.267/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.010302 € ; score 93.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : 233.48 € ; score 90.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GOAT-EUR : 0.016145 € ; score 90.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XRP-EUR : 1.33658 € ; score 86.86/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.5912 € ; score 86.41/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017291 | +121.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017 | +101.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053728 | +55.95 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.3202 | +42.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.11167 | +40.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010715 | +36.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043792 | +34.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.25804 | +23.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.066063 | +23.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.2942e-06 | +23.55 % | DETECTED_EARLY | NONE | NONE |

Historique : 1115 scans ; 477727 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
