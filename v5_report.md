# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T19:52:08.405746+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T19:51:36.966925+00:00 | âge ticker : 157.2 s | durée : 159.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 264.75 € | IGNITION | score 91.46/100 | entrée 7.65/10
  Entrée 265.07 € ; stop 253.22 € ; TP1 288.77 € ; TP2 300.62 € ; montant 232.79 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.86/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.19708 € | IGNITION | score 80.56/100 | entrée 7.80/10
  Entrée 0.19728 € ; stop 0.18969 € ; TP1 0.21246 € ; TP2 0.22005 € ; montant 250.00 € ; risque théorique 11.33 € ; R/R net 1.54.
  Chase risk : 5.149/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VVV-EUR : 28.0845 € | IGNITION | score 74.05/100 | entrée 6.55/10
  Entrée 28.0826 € ; stop 26.3416 € ; TP1 31.5646 € ; TP2 33.3056 € ; montant 9.67 € ; risque théorique 0.67 € ; R/R net 1.69.
  Chase risk : 5.54/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ARB-EUR : 0.1939 € ; score 91.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- THE-EUR : 0.07489 € ; score 88.93/100 ; SURVEILLE ; seuil achat non atteint
- IOST-EUR : 0.0008122 € ; score 88.38/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GMT-EUR : 0.007677 € ; score 86.81/100 ; SURVEILLE ; WICK_SETUP
- CVC-EUR : 0.026448 € ; score 86.42/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0097399 | +41.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38167 | +34.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.61161 | +31.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0019707 | +25.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.45008 | +24.40 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 75.438 | +20.84 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.093963 | +20.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PLUME-EUR | 0.0162576 | +19.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.037063 | +19.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.1637 | +17.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1382 scans ; 591482 observations ; 757 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
