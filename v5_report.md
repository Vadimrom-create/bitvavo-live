# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T16:23:41.720970+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-09-30T16:23:08.747184+00:00 | âge ticker : 156.8 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.05792 € | IGNITION | score 92.27/100 | entrée 7.60/10
  Entrée 1.05779 € ; stop 1.00141 € ; TP1 1.17055 € ; TP2 1.22693 € ; montant 199.62 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 4.607/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 4.7061 € | IGNITION | score 84.90/100 | entrée 6.95/10
  Entrée 4.7076 € ; stop 4.4854 € ; TP1 5.152 € ; TP2 5.3742 € ; montant 222.08 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 2.018/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PLUME-EUR : 0.0164727 € ; score 91.64/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7178 € ; score 91.08/100 ; SURVEILLE ; seuil achat non atteint
- LPT-EUR : 1.5944 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.546 € ; score 87.76/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.72462 € ; score 87.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.517 | +58.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34451 | +44.15 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.44249 | +31.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0022032 | +23.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 267.453 | +22.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.007597 | +18.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00777 | +17.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.25362 | +16.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49757 | +15.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.028561 | +14.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1849 scans ; 791148 observations ; 1393 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
