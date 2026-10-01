# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T08:27:32.183402+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 430
Récupération : 2026-10-01T08:26:53.641988+00:00 | âge ticker : 157.6 s | durée : 159.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- HUMA-EUR : 0.029158 € ; score 87.84/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- 0G-EUR : 0.27776 € ; score 83.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DIA-EUR : 0.15362 € ; score 82.94/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ALICE-EUR : 0.14978 € ; score 81.41/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- KSM-EUR : 4.5602 € ; score 81.12/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.4458 | +62.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.37009 | +54.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0025072 | +35.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.45317 | +27.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34358 | +24.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.48435 | +20.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028594 | +20.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0647744 | +19.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| JASMY-EUR | 0.0053411 | +17.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DUSK-EUR | 0.085734 | +16.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1896 scans ; 811358 observations ; 1462 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
