# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T21:40:16.069215+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T21:39:46.198467+00:00 | âge ticker : 154.3 s | durée : 155.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZORA-EUR : 0.00788 € ; score 90.80/100 ; SURVEILLE ; WICK_SETUP
- AXL-EUR : 0.047211 € ; score 85.40/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- LINK-EUR : 11.2888 € ; score 84.75/100 ; SURVEILLE ; seuil achat non atteint
- XAN-EUR : 0.010971 € ; score 84.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PROMPT-EUR : 0.019335 € ; score 84.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020085 | +35.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020095 | +29.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 298.7 | +27.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.052672 | +24.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069075 | +17.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.301979 | +17.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12122 | +17.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0088722 | +16.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.075523 | +16.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.192 | +15.19 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1218 scans ; 521605 observations ; 543 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
