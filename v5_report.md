# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T07:50:39.377965+00:00
État : OK | marchés EUR : 426 | V4 : 379 | données valides : 426
Récupération : 2026-09-21T07:50:04.061853+00:00 | âge ticker : 152.9 s | durée : 154.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- APT-EUR : 0.6707 € | IGNITION | score 79.68/100 | entrée 7.05/10
  Entrée 0.6712 € ; stop 0.6366 € ; TP1 0.7404 € ; TP2 0.7749 € ; montant 205.59 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.51/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.2778 € ; score 93.12/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ORCA-EUR : 1.28546 € ; score 86.81/100 ; SURVEILLE ; seuil achat non atteint
- LUNA-EUR : 4.6737e-05 € ; score 86.69/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PARTI-EUR : 0.022166 € ; score 84.51/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MERL-EUR : 0.023203 € ; score 84.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055106 | +65.32 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009206 | +51.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.25 | +36.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057934 | +35.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.031592 | +30.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.52442 | +27.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.753 | +24.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029272 | +24.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 29.3373 | +22.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.049804 | +19.93 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1057 scans ; 453019 observations ; 329 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
