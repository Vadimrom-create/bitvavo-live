# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T11:29:13.014991+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T11:28:20.561360+00:00 | âge ticker : 178.1 s | durée : 179.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PENGU-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7158 € | IGNITION | score 82.91/100 | entrée 7.15/10
  Entrée 1.7183 € ; stop 1.6386 € ; TP1 1.8776 € ; TP2 1.9573 € ; montant 225.48 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 4.935/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- KAS-EUR : 0.037117 € | IGNITION | score 79.96/100 | entrée 6.10/10
  Entrée 0.037242 € ; stop 0.035779 € ; TP1 0.040167 € ; TP2 0.04163 € ; montant 250.00 € ; risque théorique 11.54 € ; R/R net 1.54.
  Chase risk : 8.316/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ADA-EUR : 0.22474 € ; score 93.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.083475 € ; score 92.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 270.68 € ; score 92.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : 0.43838 € ; score 92.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 4.0227e-06 € ; score 91.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.71143 | +43.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.21412 | +40.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 85.799 | +35.02 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.1005 | +29.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48358 | +28.73 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.055007 | +27.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.088385 | +21.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.21091 | +21.37 % | DETECTED_EARLY | NONE | NONE |
| DEEP-EUR | 0.019821 | +20.54 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PEAQ-EUR | 0.038927 | +20.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1440 scans ; 616248 observations ; 832 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
