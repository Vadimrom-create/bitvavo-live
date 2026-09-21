# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:29:35.961121+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T21:29:04.059695+00:00 | âge ticker : 155.9 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : 0.39496 € | IGNITION | score 91.90/100 | entrée 8.15/10
  Entrée 0.39496 € ; stop 0.38105 € ; TP1 0.42277 € ; TP2 0.43668 € ; montant 250.00 € ; risque théorique 10.52 € ; R/R net 1.50.
  Chase risk : 2.24/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- STX-EUR : 0.2985 € | IGNITION | score 82.59/100 | entrée 7.20/10
  Entrée 0.29882 € ; stop 0.28805 € ; TP1 0.32036 € ; TP2 0.33113 € ; montant 250.00 € ; risque théorique 10.73 € ; R/R net 1.51.
  Chase risk : 4.862/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SNX-EUR : 0.20992 € ; score 83.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- APT-EUR : 0.6788 € ; score 82.46/100 ; SURVEILLE ; seuil achat non atteint
- BCH-EUR : 233.86 € ; score 81.42/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.62462 € ; score 80.45/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0048919 € ; score 80.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017375 | +122.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016532 | +96.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052498 | +52.38 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.10992 | +37.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30694 | +36.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008884 | +36.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043611 | +35.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010503 | +27.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.39159 | +25.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.258115 | +25.06 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1118 scans ; 479005 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
