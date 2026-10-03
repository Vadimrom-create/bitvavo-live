# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T00:27:48.225988+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T00:27:19.459166+00:00 | âge ticker : 149.7 s | durée : 150.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : 1.04035 € | IGNITION | score 87.67/100 | entrée 7.60/10
  Entrée 1.04013 € ; stop 0.99213 € ; TP1 1.13613 € ; TP2 1.18413 € ; montant 226.47 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.948/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 62.902 € ; score 88.68/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 261.47 € ; score 87.67/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 9.6621 € ; score 87.42/100 ; SURVEILLE ; WICK_SETUP
- ALICE-EUR : 0.15606 € ; score 87.30/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- FET-EUR : 0.19654 € ; score 87.09/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.059102 | +47.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0061 | +17.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023485 | +16.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.14901 | +11.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.029724 | +11.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.023183 | +10.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.49801 | +10.27 % | DETECTED_EARLY | NONE | NONE |
| MANA-EUR | 0.087364 | +9.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AXS-EUR | 1.0897 | +7.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00047565 | +7.28 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2016 scans ; 862802 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
