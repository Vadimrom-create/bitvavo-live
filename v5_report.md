# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-11T16:46:48.543374+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 427
Récupération : 2026-10-11T16:45:39.897237+00:00 | âge ticker : 186.7 s | durée : 187.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- RAY-EUR : 2.1546 € | IGNITION | score 84.12/100 | entrée 7.15/10
  Entrée 2.15639 € ; stop 2.04581 € ; TP1 2.37755 € ; TP2 2.48813 € ; montant 206.54 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 9.646/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.12564 € ; score 80.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- PARTI-EUR : 0.031762 € ; score 80.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.01599 € ; score 78.82/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 5.1309 € ; score 78.34/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.8228 € ; score 76.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0018555 | +89.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| S-EUR | 0.056423 | +40.23 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZEUS-EUR | 0.0082208 | +34.77 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.106211 | +25.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHIP-EUR | 0.061307 | +24.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MAGIC-EUR | 0.111436 | +21.57 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.67717 | +17.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BAT-EUR | 0.14256 | +15.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.5222 | +14.88 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ROSE-EUR | 0.008248 | +12.97 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2142 scans ; 916526 observations ; 1656 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
