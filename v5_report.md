# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T13:46:16.245676+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-21T13:45:43.654120+00:00 | âge ticker : 155.5 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- LTC-EUR : 54.567 € | IGNITION | score 76.95/100 | entrée 7.35/10
  Entrée 54.585 € ; stop 52.014 € ; TP1 59.727 € ; TP2 62.297 € ; montant 222.49 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.448/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAKE-EUR : 2.2005 € ; score 91.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ACH-EUR : 0.0052245 € ; score 86.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- XAI-EUR : 0.0069403 € ; score 85.73/100 ; SURVEILLE ; seuil achat non atteint
- UMA-EUR : 0.34793 € ; score 83.92/100 ; SURVEILLE ; seuil achat non atteint
- COW-EUR : 0.13639 € ; score 83.69/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.05386 | +63.13 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.049485 | +57.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010113 | +51.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.100678 | +33.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.24459 | +33.57 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PROVE-EUR | 0.25221 | +29.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.056251 | +29.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.91312 | +28.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.052517 | +27.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030709 | +27.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1080 scans ; 462817 observations ; 378 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
