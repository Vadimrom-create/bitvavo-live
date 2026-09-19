# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T11:17:27.360546+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 34
Récupération : 2026-09-19T11:16:58.980947+00:00 | âge ticker : 151.3 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/427 ; 15 min 79/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- RENDER-EUR : WICK_SETUP, INVALID_5M
- SHIB-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- VET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M
- WIF-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- SUI-EUR : 0.74713 € | IGNITION | score 90.54/100 | entrée 7.70/10
  Entrée 0.74752 € ; stop 0.71468 € ; TP1 0.81319 € ; TP2 0.84603 € ; montant 236.32 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.631/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.35689 € ; score 87.91/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.076553 € ; score 83.96/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.3199e-06 € ; score 81.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 79.88 € ; score 80.09/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.16832 € ; score 79.32/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.212946 | +40.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.066111 | +39.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.024315 | +34.53 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.039242 | +33.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.076179 | +31.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.148606 | +31.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036976 | +28.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.046874 | +25.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.29274 | +25.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.39 | +24.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 884 scans ; 379247 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
