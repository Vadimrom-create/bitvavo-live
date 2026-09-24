# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T03:55:43.784041+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T03:55:14.080358+00:00 | âge ticker : 155.4 s | durée : 156.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- ETC-EUR : 7.9787 € | IGNITION | score 88.92/100 | entrée 6.50/10
  Entrée 7.9965 € ; stop 7.5998 € ; TP1 8.7899 € ; TP2 9.1866 € ; montant 212.63 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.897/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LTC-EUR : 58.79 € | IGNITION | score 80.86/100 | entrée 6.80/10
  Entrée 58.791 € ; stop 53.9 € ; TP1 68.573 € ; TP2 73.464 € ; montant 133.48 € ; risque théorique 12.00 € ; R/R net 1.77.
  Chase risk : 9.843/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MOVR-EUR : 0.7765 € ; score 88.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.056036 € ; score 87.59/100 ; SURVEILLE ; WICK_SETUP
- DOT-EUR : 0.9785 € ; score 87.04/100 ; SURVEILLE ; WICK_SETUP
- ACU-EUR : 0.11065 € ; score 86.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PLUME-EUR : 0.0140526 € ; score 85.75/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021237 | +37.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.116845 | +35.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018797 | +14.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.040227 | +14.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.31189 | +12.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.028942 | +11.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28802 | +9.60 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| KMNO-EUR | 0.032849 | +7.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3484 | +6.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0017002 | +6.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1326 scans ; 567613 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
