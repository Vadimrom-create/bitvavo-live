# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T10:52:05.557756+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T10:51:35.417318+00:00 | âge ticker : 146.6 s | durée : 147.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.106305 € | IGNITION | score 89.40/100 | entrée 6.90/10
  Entrée 0.106168 € ; stop 0.100168 € ; TP1 0.118168 € ; TP2 0.124168 € ; montant 189.52 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 4.65/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- GALA-EUR : 0.0019521 € | IGNITION | score 85.77/100 | entrée 7.45/10
  Entrée 0.0019535 € ; stop 0.0018816 € ; TP1 0.0020973 € ; TP2 0.0021691 € ; montant 250.00 € ; risque théorique 10.92 € ; R/R net 1.52.
  Chase risk : 4.526/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- OP-EUR : 0.12876 € | IGNITION | score 85.00/100 | entrée 7.00/10
  Entrée 0.12892 € ; stop 0.12411 € ; TP1 0.13854 € ; TP2 0.14335 € ; montant 24.46 € ; risque théorique 1.08 € ; R/R net 1.52.
  Chase risk : 2.477/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WLD-EUR : 0.42629 € ; score 93.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.069258 € ; score 90.55/100 ; SURVEILLE ; seuil achat non atteint
- ILV-EUR : 3.5969 € ; score 90.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MOG-EUR : 1.1116e-07 € ; score 89.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TAO-EUR : 279.08 € ; score 88.41/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019974 | +155.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.021065 | +78.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.064718 | +33.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.070216 | +30.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.24968 | +24.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24292 | +17.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.80186 | +17.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.6215 | +16.34 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| KMNO-EUR | 0.039154 | +14.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.097753 | +13.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1525 scans ; 652543 observations ; 975 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
