# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T11:00:38.735311+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-21T10:59:40.161573+00:00 | âge ticker : 176.7 s | durée : 177.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.3919 € | IGNITION | score 91.29/100 | entrée 8.40/10
  Entrée 0.39189 € ; stop 0.37618 € ; TP1 0.42331 € ; TP2 0.43902 € ; montant 250.00 € ; risque théorique 11.74 € ; R/R net 1.55.
  Chase risk : 4.417/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CTSI-EUR : 0.02586 € ; score 90.95/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ENS-EUR : 5.8219 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- BCH-EUR : 232.38 € ; score 88.62/100 ; SURVEILLE ; seuil achat non atteint
- IOST-EUR : 0.0007741 € ; score 88.62/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZRX-EUR : 0.102494 € ; score 86.52/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.057162 | +84.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.056782 | +73.04 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.000985 | +55.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.058656 | +36.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.055176 | +33.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030359 | +29.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.031323 | +25.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.22749 | +24.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SUI-EUR | 0.87192 | +23.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.03033 | +22.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1070 scans ; 458557 observations ; 353 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
