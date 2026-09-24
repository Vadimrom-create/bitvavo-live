# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T14:04:21.956677+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T14:03:23.235381+00:00 | âge ticker : 186.8 s | durée : 188.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0081844 € | IGNITION | score 85.52/100 | entrée 6.85/10
  Entrée 0.0081906 € ; stop 0.0077993 € ; TP1 0.0089731 € ; TP2 0.0093644 € ; montant 219.75 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 7.104/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RENDER-EUR : 1.6084 € | IGNITION | score 85.28/100 | entrée 7.00/10
  Entrée 1.6121 € ; stop 1.5524 € ; TP1 1.7315 € ; TP2 1.7912 € ; montant 250.00 € ; risque théorique 10.98 € ; R/R net 1.52.
  Chase risk : 3.477/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PYTH-EUR : 0.05812 € | IGNITION | score 82.79/100 | entrée 7.00/10
  Entrée 0.058129 € ; stop 0.055229 € ; TP1 0.063929 € ; TP2 0.066829 € ; montant 18.06 € ; risque théorique 1.02 € ; R/R net 1.63.
  Chase risk : 5.495/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- UNI-EUR : 8.0702 € ; score 91.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DRIFT-EUR : 0.016118 € ; score 91.44/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.00685 € ; score 90.12/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ADA-EUR : 0.2129 € ; score 89.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034434 € ; score 89.30/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0022283 | +44.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.36405 | +32.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.100504 | +27.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.42938 | +13.42 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 62.353 | +12.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.21534 | +12.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MORPHO-EUR | 2.5387 | +12.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.08686 | +12.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMU-EUR | 0.0018881 | +9.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.15474 | +8.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1360 scans ; 582097 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
