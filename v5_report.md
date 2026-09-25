# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T11:09:11.629156+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T11:08:42.888865+00:00 | âge ticker : 152.9 s | durée : 154.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ARB-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PENGU-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : 1.7206 € | IGNITION | score 85.52/100 | entrée 7.45/10
  Entrée 1.7211 € ; stop 1.6394 € ; TP1 1.8845 € ; TP2 1.9662 € ; montant 220.98 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 3.561/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.082702 € ; score 91.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.036749 € ; score 90.40/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : 0.0041084 € ; score 89.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PENGU-EUR : 0.0088157 € ; score 88.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 106.262 € ; score 87.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.71229 | +41.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 86.475 | +35.67 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.2065 | +35.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.101115 | +30.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48499 | +29.44 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.054526 | +28.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.038808 | +20.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20909 | +19.95 % | DETECTED_EARLY | NONE | NONE |
| JTO-EUR | 0.48279 | +19.71 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| DBR-EUR | 0.02118 | +19.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1439 scans ; 615821 observations ; 829 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
