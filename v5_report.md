# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T03:34:11.287758+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T03:33:38.904321+00:00 | âge ticker : 149.8 s | durée : 150.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.10623 € ; score 90.78/100 ; SURVEILLE ; SPREAD_RISK
- KAITO-EUR : 0.30532 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AZTEC-EUR : 0.013731 € ; score 86.48/100 ; SURVEILLE ; seuil achat non atteint
- BOME-EUR : 0.00093935 € ; score 86.27/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- LDO-EUR : 0.37226 € ; score 85.37/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017 | +97.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013276 | +70.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.058612 | +56.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.05496 | +48.60 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.111991 | +41.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.047182 | +39.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5313e-06 | +29.24 % | DETECTED_EARLY | NONE | NONE |
| CARV-EUR | 0.041133 | +25.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WIF-EUR | 0.21646 | +22.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.26937 | +18.12 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1145 scans ; 490507 observations ; 449 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
