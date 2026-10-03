# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T01:10:36.816729+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T01:09:41.578733+00:00 | âge ticker : 176.6 s | durée : 177.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : 1.05272 € | IGNITION | score 83.09/100 | entrée 7.60/10
  Entrée 1.05304 € ; stop 0.99576 € ; TP1 1.1676 € ; TP2 1.22488 € ; montant 196.06 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 6.462/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SYRUP-EUR : 0.2167 € ; score 92.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.114218 € ; score 92.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 62.973 € ; score 89.28/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.7145 € ; score 88.59/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GRASS-EUR : 0.64 € ; score 88.43/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.061363 | +54.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023826 | +18.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENJ-EUR | 0.030938 | +15.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089587 | +12.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.005864 | +12.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.46966 | +12.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50038 | +11.51 % | DETECTED_EARLY | NONE | NONE |
| APE-EUR | 0.14846 | +10.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.023049 | +9.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UP-EUR | 0.066136 | +9.71 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2018 scans ; 863654 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
