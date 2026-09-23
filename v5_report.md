# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T12:11:17.285727+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-23T12:10:46.991751+00:00 | âge ticker : 144.1 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : 2.7507 € | IGNITION | score 92.48/100 | entrée 7.70/10
  Entrée 2.7643 € ; stop 2.6566 € ; TP1 2.9797 € ; TP2 3.0873 € ; montant 250.00 € ; risque théorique 11.46 € ; R/R net 1.54.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- NEWT-EUR : 0.044463 € ; score 91.31/100 ; SURVEILLE ; seuil achat non atteint
- ONG-EUR : 0.079615 € ; score 89.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SHELL-EUR : 0.025088 € ; score 88.63/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- LTC-EUR : 54.485 € ; score 85.20/100 ; SURVEILLE ; WICK_SETUP
- MANTA-EUR : 0.062157 € ; score 84.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034586 | +44.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.35373 | +37.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.297419 | +32.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 301 | +26.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.085581 | +24.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2851 | +22.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018723 | +21.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.1593 | +21.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.020017 | +21.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.040899 | +19.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1268 scans ; 542905 observations ; 643 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
