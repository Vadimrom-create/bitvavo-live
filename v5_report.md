# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T05:25:03.468836+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-10-01T05:24:34.309023+00:00 | âge ticker : 154.3 s | durée : 155.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : 0.73965 € | IGNITION | score 90.86/100 | entrée 7.65/10
  Entrée 0.74108 € ; stop 0.71211 € ; TP1 0.79901 € ; TP2 0.82798 € ; montant 250.00 € ; risque théorique 11.49 € ; R/R net 1.54.
  Chase risk : 3.308/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- MEGA-EUR : 0.03985 € | IGNITION | score 80.51/100 | entrée 6.80/10
  Entrée 0.03986 € ; stop 0.03831 € ; TP1 0.04296 € ; TP2 0.04451 € ; montant 250.00 € ; risque théorique 11.44 € ; R/R net 1.54.
  Chase risk : 4.521/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PYTH-EUR : 0.06937 € ; score 91.82/100 ; SURVEILLE ; seuil achat non atteint
- HUMA-EUR : 0.028467 € ; score 91.41/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- TAO-EUR : 272.03 € ; score 89.72/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EPIC-EUR : 0.47794 € ; score 88.47/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 105.353 € ; score 86.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.2785 | +77.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34459 | +44.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009038 | +31.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.4425 | +27.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34718 | +24.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029026 | +22.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0634913 | +18.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PLUME-EUR | 0.0183738 | +16.97 % | DETECTED_EARLY | NONE | NONE |
| MOVE-EUR | 0.009256 | +15.18 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RED-EUR | 0.16218 | +14.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1888 scans ; 807918 observations ; 1443 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
