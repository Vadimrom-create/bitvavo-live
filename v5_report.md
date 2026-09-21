# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T01:39:02.601642+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-21T01:38:31.796107+00:00 | âge ticker : 153.7 s | durée : 154.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PHA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.08098 € | IGNITION | score 78.65/100 | entrée 7.45/10
  Entrée 0.081179 € ; stop 0.077131 € ; TP1 0.089275 € ; TP2 0.093322 € ; montant 211.68 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.014/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RED-EUR : 0.13239 € ; score 90.01/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- LPT-EUR : 1.4098 € ; score 89.07/100 ; SURVEILLE ; WICK_SETUP
- AVNT-EUR : 0.09573 € ; score 87.45/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 232.05 € ; score 87.21/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINEA-EUR : 0.0024128 € ; score 85.65/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.033323 | +48.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008573 | +38.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.246 | +32.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49314 | +24.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.054517 | +23.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.029342 | +21.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6276 | +18.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.126761 | +17.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 26.8452 | +17.30 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| S-EUR | 0.033455 | +15.57 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1037 scans ; 444499 observations ; 286 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
