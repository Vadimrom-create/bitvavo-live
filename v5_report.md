# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T08:45:20.275037+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T08:44:49.716315+00:00 | âge ticker : 153.3 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.105009 € | IGNITION | score 87.53/100 | entrée 6.90/10
  Entrée 0.105194 € ; stop 0.097805 € ; TP1 0.119971 € ; TP2 0.12736 € ; montant 155.85 € ; risque théorique 12.00 € ; R/R net 1.73.
  Chase risk : 8.908/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- 0G-EUR : 0.23082 € ; score 93.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.0389 € ; score 93.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.142877 € ; score 92.97/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.43201 € ; score 92.00/100 ; SURVEILLE ; STABILITY_HOLD
- CHR-EUR : 0.019066 € ; score 90.47/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017623 | +124.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018869 | +63.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.067948 | +36.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.064419 | +33.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24875 | +28.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24445 | +25.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78583 | +19.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038404 | +16.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.003952 | +16.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.56 | +16.07 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1517 scans ; 649127 observations ; 965 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
