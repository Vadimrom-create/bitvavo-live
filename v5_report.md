# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T19:20:22.110618+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T19:19:45.617916+00:00 | âge ticker : 150.1 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0078885 € | IGNITION | score 82.75/100 | entrée 7.75/10
  Entrée 0.0078786 € ; stop 0.0075929 € ; TP1 0.00845 € ; TP2 0.0087356 € ; montant 250.00 € ; risque théorique 10.78 € ; R/R net 1.51.
  Chase risk : 3.133/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XTZ-EUR : 0.30455 € ; score 91.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GRASS-EUR : 0.32439 € ; score 89.73/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- MORPHO-EUR : 2.34114 € ; score 88.38/100 ; SURVEILLE ; seuil achat non atteint
- POWR-EUR : 0.055432 € ; score 85.62/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- SUPER-EUR : 0.13115 € ; score 82.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.00178 | +131.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.014526 | +72.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.054 | +59.25 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.045909 | +43.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30614 | +36.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.108215 | +35.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008668 | +33.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010265 | +32.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.235062 | +26.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3569e-06 | +24.82 % | DETECTED_EARLY | NONE | NONE |

Historique : 1105 scans ; 473467 observations ; 403 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
