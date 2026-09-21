# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T09:36:16.594747+00:00
État : OK | marchés EUR : 426 | V4 : 377 | données valides : 426
Récupération : 2026-09-21T09:35:47.417213+00:00 | âge ticker : 144.5 s | durée : 146.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- EIGEN-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- ENA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- TIA-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- WIF-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- XLM-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- PEPE-EUR : 3.6824e-06 € | IGNITION | score 87.34/100 | entrée 7.65/10
  Entrée 3.6864e-06 € ; stop 3.4639e-06 € ; TP1 4.1314e-06 € ; TP2 4.3539e-06 € ; montant 178.72 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 5.562/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XPL-EUR : 0.085202 € | IGNITION | score 84.90/100 | entrée 7.40/10
  Entrée 0.085224 € ; stop 0.080589 € ; TP1 0.094494 € ; TP2 0.099129 € ; montant 196.09 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 4.753/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ARX-EUR : 0.17391 € ; score 93.67/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- INJ-EUR : 6.8868 € ; score 93.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.1257 € ; score 92.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ATH-EUR : 0.0047811 € ; score 91.55/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0017701 € ; score 89.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.057196 | +73.41 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.04884 | +56.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009582 | +54.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.060027 | +38.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.032504 | +32.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.2376 | +29.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.03017 | +28.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.032 | +27.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.51387 | +25.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.015885 | +24.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1064 scans ; 456001 observations ; 337 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
