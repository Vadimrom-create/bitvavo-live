# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T22:45:44.802813+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T22:45:15.041029+00:00 | âge ticker : 155.3 s | durée : 156.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : BELOW_EXCHANGE_MINIMUM
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25178 € | IGNITION | score 92.68/100 | entrée 7.75/10
  Entrée 0.25187 € ; stop 0.2409 € ; TP1 0.2738 € ; TP2 0.28477 € ; montant 238.09 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.136/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.38049 € | IGNITION | score 90.89/100 | entrée 7.65/10
  Entrée 0.38068 € ; stop 0.36346 € ; TP1 0.41512 € ; TP2 0.43234 € ; montant 230.43 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.947/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MIRA-EUR : 0.045322 € ; score 89.67/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.006659 € ; score 89.52/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD
- SKY-EUR : 0.062053 € ; score 88.81/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.094305 € ; score 88.32/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.022894 € ; score 87.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.031857 | +44.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24428 | +32.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0008097 | +32.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.056465 | +27.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49837 | +22.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028723 | +19.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.034487 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.048601 | +16.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.8193 | +15.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.125499 | +15.67 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1025 scans ; 439387 observations ; 276 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
