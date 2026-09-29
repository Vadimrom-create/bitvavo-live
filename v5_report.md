# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T09:26:16.542442+00:00
État : OK | marchés EUR : 428 | V4 : 393 | données valides : 428
Récupération : 2026-09-29T09:25:42.508057+00:00 | âge ticker : 156.7 s | durée : 157.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XDC-EUR : 0.0314 € | IGNITION | score 82.85/100 | entrée 5.95/10
  Entrée 0.031516 € ; stop 0.03026 € ; TP1 0.034028 € ; TP2 0.035284 € ; montant 250.00 € ; risque théorique 11.68 € ; R/R net 1.55.
  Chase risk : 7.537/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.11174 € ; score 88.26/100 ; SURVEILLE ; WICK_SETUP
- AKT-EUR : 0.58611 € ; score 86.16/100 ; SURVEILLE ; seuil achat non atteint
- IMX-EUR : 0.15122 € ; score 80.97/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- COMP-EUR : 22.181 € ; score 80.88/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- GALA-EUR : 0.0019996 € ; score 80.69/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00181 | +46.04 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.1592 | +27.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.3539 | +23.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.088799 | +18.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0719 | +18.48 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CELO-EUR | 0.0936 | +18.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.26538 | +17.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.5989 | +16.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.30766 | +16.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.21079 | +15.48 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1759 scans ; 752525 observations ; 1287 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
