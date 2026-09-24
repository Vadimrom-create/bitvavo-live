# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T03:40:44.499770+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T03:40:15.571578+00:00 | âge ticker : 161.9 s | durée : 162.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 7.9118 € | IGNITION | score 93.00/100 | entrée 7.15/10
  Entrée 7.9382 € ; stop 7.6021 € ; TP1 8.6104 € ; TP2 8.9465 € ; montant 243.95 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.239/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LTC-EUR : 58.324 € | IGNITION | score 82.36/100 | entrée 7.20/10
  Entrée 58.38 € ; stop 53.931 € ; TP1 67.278 € ; TP2 71.727 € ; montant 144.68 € ; risque théorique 12.00 € ; R/R net 1.75.
  Chase risk : 9.08/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- A-EUR : 0.081655 € ; score 92.63/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.079553 € ; score 88.19/100 ; SURVEILLE ; seuil achat non atteint
- SOSO-EUR : 0.2881 € ; score 86.51/100 ; SURVEILLE ; LOW_LIQUIDITY
- SUSHI-EUR : 0.22096 € ; score 85.67/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.056579 € ; score 85.35/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0020459 | +33.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.116084 | +28.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.040545 | +15.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018786 | +15.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.31837 | +15.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.028512 | +10.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.2881 | +8.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| KMNO-EUR | 0.032973 | +8.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COTI-EUR | 0.014469 | +6.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0443229 | +6.62 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1325 scans ; 567187 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
