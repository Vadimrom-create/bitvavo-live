# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T08:56:35.924431+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-02T08:56:06.956224+00:00 | âge ticker : 155.2 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : 0.116661 € | IGNITION | score 79.75/100 | entrée 6.95/10
  Entrée 0.116517 € ; stop 0.111624 € ; TP1 0.126303 € ; TP2 0.131195 € ; montant 245.67 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.336/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- EIGEN-EUR : 0.23085 € | IGNITION | score 78.23/100 | entrée 7.20/10
  Entrée 0.23094 € ; stop 0.22268 € ; TP1 0.24746 € ; TP2 0.25572 € ; montant 250.00 € ; risque théorique 10.66 € ; R/R net 1.51.
  Chase risk : 3.298/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- POND-EUR : 0.0014601 € ; score 88.00/100 ; SURVEILLE ; WICK_SETUP
- XAI-EUR : 0.0086126 € ; score 87.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEO-EUR : 2.2989 € ; score 86.49/100 ; SURVEILLE ; seuil achat non atteint
- PTB-EUR : 0.0008394 € ; score 85.04/100 ; SURVEILLE ; STABILITY_HOLD
- ID-EUR : 0.03352 € ; score 85.02/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00072 | +175.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.54398 | +45.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.055504 | +42.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.113503 | +28.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.026863 | +18.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6632 | +14.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20102 | +13.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.089112 | +12.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MAGIC-EUR | 0.052488 | +11.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.226077 | +11.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1968 scans ; 842318 observations ; 1553 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
