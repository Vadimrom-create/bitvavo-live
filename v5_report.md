# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T04:46:19.150352+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-10-01T04:45:49.284173+00:00 | âge ticker : 151.1 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.7775 € | IGNITION | score 80.51/100 | entrée 7.60/10
  Entrée 4.774 € ; stop 4.5792 € ; TP1 5.1636 € ; TP2 5.3584 € ; montant 250.00 € ; risque théorique 11.92 € ; R/R net 1.56.
  Chase risk : 2.967/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DYDX-EUR : 0.12772 € ; score 92.45/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.093829 € ; score 91.60/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.039169 € ; score 90.75/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.34745 € ; score 90.71/100 ; SURVEILLE ; seuil achat non atteint
- INIT-EUR : 0.092023 € ; score 90.45/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.9522 | +71.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35445 | +48.31 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.43641 | +27.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008539 | +26.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.34591 | +24.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028476 | +21.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0184673 | +17.32 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.0620597 | +16.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAFE-EUR | 0.110284 | +15.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009166 | +14.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1886 scans ; 807058 observations ; 1438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
