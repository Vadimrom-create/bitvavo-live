# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T16:19:50.803487+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 33
Récupération : 2026-09-20T16:19:23.200106+00:00 | âge ticker : 140.5 s | durée : 142.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 34/426 ; 15 min 75/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- BNB-EUR : WICK_SETUP, INVALID_5M
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INVALID_5M
- QNT-EUR : INVALID_15M, INVALID_5M
- RAY-EUR : INVALID_5M
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- SHIB-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.74507 € | IGNITION | score 86.07/100 | entrée 7.20/10
  Entrée 0.74463 € ; stop 0.70885 € ; TP1 0.81619 € ; TP2 0.85197 € ; montant 218.65 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 4.844/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.36863 € | IGNITION | score 80.55/100 | entrée 7.65/10
  Entrée 0.36865 € ; stop 0.35315 € ; TP1 0.39964 € ; TP2 0.41514 € ; montant 245.41 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.829/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 95.183 € ; score 89.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.649 € ; score 82.48/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.19722 € ; score 81.22/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0072648 € ; score 79.54/100 ; SURVEILLE ; WICK_SETUP
- HBAR-EUR : 0.076806 € ; score 77.16/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| FTT-EUR | 0.28261 | +57.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CELR-EUR | 0.0031392 | +40.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.50492 | +23.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.027038 | +23.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.000745 | +22.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.8474 | +18.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.047695 | +14.11 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ALGO-EUR | 0.099748 | +13.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.5234 | +13.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| C-EUR | 0.068227 | +10.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 994 scans ; 426181 observations ; 234 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
