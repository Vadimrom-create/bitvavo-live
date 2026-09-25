# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T09:57:07.653595+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T09:56:42.402616+00:00 | âge ticker : 146.6 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KMNO-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.019308 € | IGNITION | score 92.22/100 | entrée 7.05/10
  Entrée 0.019331 € ; stop 0.018494 € ; TP1 0.021005 € ; TP2 0.021842 € ; montant 239.30 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.183/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ETC-EUR : 8.4391 € ; score 91.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.084952 € ; score 88.70/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LIGHTER-EUR : 4.3892 € ; score 87.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MIOTA-EUR : 0.043082 € ; score 86.92/100 ; SURVEILLE ; seuil achat non atteint
- A-EUR : 0.087423 € ; score 86.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.765 | +53.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 84.782 | +36.48 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.49022 | +31.13 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.101531 | +31.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.053137 | +26.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.18578 | +24.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.038916 | +22.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20665 | +20.50 % | DETECTED_EARLY | NONE | NONE |
| CHIP-EUR | 0.04332 | +20.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021203 | +18.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1435 scans ; 614113 observations ; 826 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
