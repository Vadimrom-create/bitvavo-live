# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T11:54:10.561413+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-09-21T11:53:38.860821+00:00 | âge ticker : 154.9 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : 3.6891e-06 € | IGNITION | score 87.47/100 | entrée 7.40/10
  Entrée 3.6903e-06 € ; stop 3.5581e-06 € ; TP1 3.9547e-06 € ; TP2 4.0869e-06 € ; montant 250.00 € ; risque théorique 10.67 € ; R/R net 1.51.
  Chase risk : 4.495/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAO-EUR : 247.49 € | IGNITION | score 81.02/100 | entrée 7.60/10
  Entrée 247.63 € ; stop 238.7 € ; TP1 265.49 € ; TP2 274.42 € ; montant 250.00 € ; risque théorique 10.73 € ; R/R net 1.51.
  Chase risk : 4.155/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.39176 € | IGNITION | score 77.97/100 | entrée 7.70/10
  Entrée 0.39169 € ; stop 0.37601 € ; TP1 0.42304 € ; TP2 0.43872 € ; montant 55.27 € ; risque théorique 2.59 € ; R/R net 1.55.
  Chase risk : 4.217/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MERL-EUR : 0.023911 € ; score 93.70/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.030069 € ; score 87.39/100 ; SURVEILLE ; seuil achat non atteint
- KAITO-EUR : 0.30297 € ; score 85.93/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GRASS-EUR : 0.32507 € ; score 85.73/100 ; SURVEILLE ; WICK_SETUP
- NEO-EUR : 2.1898 € ; score 85.35/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.057149 | +71.71 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.051286 | +62.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.001013 | +33.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.056576 | +31.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.031188 | +29.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.053386 | +28.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23387 | +27.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.031877 | +24.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.88853 | +24.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHIP-EUR | 0.043609 | +22.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1073 scans ; 459835 observations ; 354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
