# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T07:59:39.839880+00:00
État : OK | marchés EUR : 428 | V4 : 391 | données valides : 428
Récupération : 2026-09-29T07:59:13.600834+00:00 | âge ticker : 153.9 s | durée : 154.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- XLM-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : 276.12 € | IGNITION | score 87.67/100 | entrée 7.40/10
  Entrée 276.01 € ; stop 264.61 € ; TP1 298.8 € ; TP2 310.2 € ; montant 249.18 € ; risque théorique 12.00 € ; R/R net 1.56.
  Chase risk : 4.312/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 7.8634 € | IGNITION | score 87.55/100 | entrée 7.90/10
  Entrée 7.8646 € ; stop 7.5615 € ; TP1 8.4708 € ; TP2 8.7739 € ; montant 250.00 € ; risque théorique 11.35 € ; R/R net 1.54.
  Chase risk : 4.356/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- GALA-EUR : 0.001995 € | IGNITION | score 84.50/100 | entrée 7.25/10
  Entrée 0.0019951 € ; stop 0.0018964 € ; TP1 0.0021925 € ; TP2 0.0022912 € ; montant 11.52 € ; risque théorique 0.65 € ; R/R net 1.63.
  Chase risk : 6.666/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- NOM-EUR : 0.0018226 € ; score 90.02/100 ; SURVEILLE ; seuil achat non atteint
- HUMA-EUR : 0.025238 € ; score 89.98/100 ; SURVEILLE ; WICK_SETUP
- SUPER-EUR : 0.17145 € ; score 89.67/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7173 € ; score 89.59/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BEAM-EUR : 0.0018183 € ; score 88.51/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.3103 | +30.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.001575 | +25.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.34971 | +22.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.103012 | +20.73 % | DETECTED_EARLY | NONE | NONE |
| CELO-EUR | 0.092946 | +16.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.61129 | +15.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.23829 | +15.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.059815 | +14.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.14869 | +14.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 2.9646 | +14.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1755 scans ; 750813 observations ; 1284 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
