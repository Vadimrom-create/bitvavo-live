# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T15:48:02.214558+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-21T15:47:28.958864+00:00 | âge ticker : 154.9 s | durée : 155.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0077763 € | IGNITION | score 78.73/100 | entrée 7.30/10
  Entrée 0.0077791 € ; stop 0.0074544 € ; TP1 0.0084284 € ; TP2 0.0087532 € ; montant 246.94 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 1.981/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- NOT-EUR : 0.00043992 € ; score 89.47/100 ; SURVEILLE ; WICK_SETUP
- CC-EUR : 0.10168 € ; score 87.84/100 ; SURVEILLE ; WICK_SETUP
- RSR-EUR : 0.001428 € ; score 86.47/100 ; SURVEILLE ; seuil achat non atteint
- THE-EUR : 0.06813 € ; score 85.60/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.275 € ; score 84.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0024534 | +215.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.052568 | +58.62 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.042738 | +33.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.2523 | +33.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.10016 | +32.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.057275 | +30.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0009261 | +29.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEPE-EUR | 4.3371e-06 | +26.02 % | DETECTED_EARLY | NONE | NONE |
| KMNO-EUR | 0.030609 | +23.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21456 | +23.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1087 scans ; 465799 observations ; 386 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
