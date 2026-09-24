# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T19:27:34.061083+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T19:27:04.013747+00:00 | âge ticker : 147.6 s | durée : 149.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VVV-EUR : 27.7903 € | IGNITION | score 88.76/100 | entrée 7.10/10
  Entrée 27.7065 € ; stop 26.3337 € ; TP1 30.452 € ; TP2 31.8248 € ; montant 212.86 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.845/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GMT-EUR : 0.007688 € ; score 91.59/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.18755 € ; score 90.67/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- MMT-EUR : 0.151 € ; score 89.58/100 ; SURVEILLE ; LOW_LIQUIDITY
- HYPE-EUR : 83.241 € ; score 88.45/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- A-EUR : 0.087092 € ; score 88.25/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0101201 | +46.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.37888 | +34.92 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NOM-EUR | 0.0020148 | +29.44 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ONDO-EUR | 0.45341 | +24.95 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 76.054 | +21.80 % | DETECTED_EARLY | NONE | NONE |
| PLUME-EUR | 0.016568 | +21.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.037238 | +19.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.091863 | +18.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.572 | +17.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 62.728 | +16.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1379 scans ; 590201 observations ; 757 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
