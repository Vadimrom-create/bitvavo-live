# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T23:46:19.661678+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-20T23:45:45.829066+00:00 | âge ticker : 149.8 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25928 € | IGNITION | score 83.76/100 | entrée 7.45/10
  Entrée 0.25991 € ; stop 0.24589 € ; TP1 0.28794 € ; TP2 0.30196 € ; montant 197.52 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 7.239/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NPC-EUR : 0.021286 € | IGNITION | score 79.85/100 | entrée 7.20/10
  Entrée 0.0212858 € ; stop 0.0204529 € ; TP1 0.0229516 € ; TP2 0.0237845 € ; montant 250.00 € ; risque théorique 11.50 € ; R/R net 1.54.
  Chase risk : 2.362/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- POL-EUR : 0.095508 € | IGNITION | score 79.54/100 | entrée 6.55/10
  Entrée 0.095627 € ; stop 0.091999 € ; TP1 0.102883 € ; TP2 0.106511 € ; montant 11.20 € ; risque théorique 0.50 € ; R/R net 1.53.
  Chase risk : 3.592/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SENT-EUR : 0.015802 € ; score 90.18/100 ; SURVEILLE ; LOW_LIQUIDITY
- THE-EUR : 0.06682 € ; score 89.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HBAR-EUR : 0.075649 € ; score 88.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PROVE-EUR : 0.19965 € ; score 86.96/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- IOST-EUR : 0.0007642 € ; score 84.66/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032368 | +48.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24868 | +34.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.000797 | +30.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.054312 | +24.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.029577 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49075 | +21.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.050296 | +20.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.034466 | +18.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6401 | +16.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.126184 | +15.32 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1030 scans ; 441517 observations ; 278 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
