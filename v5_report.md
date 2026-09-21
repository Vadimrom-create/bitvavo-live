# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T20:39:35.685247+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T20:39:08.561148+00:00 | âge ticker : 150.3 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.29773 € | IGNITION | score 90.92/100 | entrée 7.55/10
  Entrée 0.29778 € ; stop 0.2858 € ; TP1 0.32173 € ; TP2 0.33371 € ; montant 250.00 € ; risque théorique 11.77 € ; R/R net 1.55.
  Chase risk : 5.277/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VET-EUR : 0.0079913 € | IGNITION | score 82.86/100 | entrée 7.45/10
  Entrée 0.0079859 € ; stop 0.0076764 € ; TP1 0.0086049 € ; TP2 0.0089144 € ; montant 250.00 € ; risque théorique 11.41 € ; R/R net 1.54.
  Chase risk : 4.269/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.40314 € | IGNITION | score 82.72/100 | entrée 7.20/10
  Entrée 0.40342 € ; stop 0.3747 € ; TP1 0.46086 € ; TP2 0.48958 € ; montant 10.55 € ; risque théorique 0.82 € ; R/R net 1.73.
  Chase risk : 6.678/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LDO-EUR : 0.37964 € ; score 91.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.39056 € ; score 90.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MANA-EUR : 0.074317 € ; score 90.36/100 ; SURVEILLE ; seuil achat non atteint
- BCH-EUR : 232.91 € ; score 90.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.605 € ; score 88.80/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017016 | +117.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015752 | +86.95 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053956 | +56.61 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.113484 | +43.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31666 | +41.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.044286 | +35.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010659 | +34.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.33886 | +26.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.261628 | +24.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008074 | +24.23 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1113 scans ; 476875 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
