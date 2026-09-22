# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T01:50:56.011355+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T01:50:00.846016+00:00 | âge ticker : 178.4 s | durée : 179.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0039204 € | IGNITION | score 79.07/100 | entrée 7.40/10
  Entrée 0.0039213 € ; stop 0.0037802 € ; TP1 0.0042035 € ; TP2 0.0043446 € ; montant 250.00 € ; risque théorique 10.71 € ; R/R net 1.51.
  Chase risk : 3.652/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.03836 € ; score 90.09/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- METIS-EUR : 3.1059 € ; score 89.97/100 ; SURVEILLE ; seuil achat non atteint
- MMT-EUR : 0.14681 € ; score 88.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AVNT-EUR : 0.1034 € ; score 87.41/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023848 € ; score 86.15/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01623 | +88.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014412 | +84.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.057592 | +56.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.050958 | +49.35 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.110071 | +38.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31156 | +36.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.044032 | +32.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.4345e-06 | +25.78 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21455 | +22.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.0259 | +20.21 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1139 scans ; 487951 observations ; 442 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
