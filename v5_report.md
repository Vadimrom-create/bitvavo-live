# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T01:30:16.003219+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T01:29:43.796388+00:00 | âge ticker : 149.9 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : 1.05439 € | IGNITION | score 85.46/100 | entrée 7.40/10
  Entrée 1.0538 € ; stop 1.00266 € ; TP1 1.15608 € ; TP2 1.20722 € ; montant 216.77 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.649/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 160.15 € ; score 93.97/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.21713 € ; score 92.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.114629 € ; score 90.24/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- MEGA-EUR : 0.04192 € ; score 89.59/100 ; SURVEILLE ; seuil achat non atteint
- PEAQ-EUR : 0.03576 € ; score 85.96/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.061999 | +57.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032271 | +20.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023776 | +17.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.005932 | +13.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.47277 | +13.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089278 | +12.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.50208 | +11.21 % | DETECTED_EARLY | NONE | NONE |
| APE-EUR | 0.14814 | +10.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.023027 | +8.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.53563 | +8.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2019 scans ; 864080 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
