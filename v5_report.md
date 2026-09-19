# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T11:32:26.276777+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 36
Récupération : 2026-09-19T11:31:56.648696+00:00 | âge ticker : 151.6 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/427 ; 15 min 77/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INVALID_5M
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INVALID_5M
- PYTH-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- RENDER-EUR : STABILITY_HOLD, INVALID_5M
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- SUI-EUR : 0.7506 € | IGNITION | score 90.43/100 | entrée 7.70/10
  Entrée 0.75035 € ; stop 0.71453 € ; TP1 0.82198 € ; TP2 0.8578 € ; montant 219.90 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 5.945/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PEPE-EUR : 3.3209e-06 € ; score 88.03/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.15951 € ; score 86.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.19183 € ; score 83.79/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.19671 € ; score 83.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 0.9805 € ; score 82.72/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.215279 | +41.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.066944 | +39.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.039884 | +35.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.077384 | +33.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.023917 | +32.33 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| HEI-EUR | 0.14609 | +28.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.003692 | +28.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.393 | +25.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046743 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.28662 | +22.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 885 scans ; 379674 observations ; 194 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
