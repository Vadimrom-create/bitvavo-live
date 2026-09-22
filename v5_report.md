# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T02:41:12.532573+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T02:40:43.089554+00:00 | âge ticker : 157.3 s | durée : 159.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.013066 € ; score 88.55/100 ; SURVEILLE ; seuil achat non atteint
- ALLO-EUR : 0.230144 € ; score 87.50/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- RON-EUR : 0.05524 € ; score 86.12/100 ; SURVEILLE ; LOW_LIQUIDITY
- STRAX-EUR : 0.010017 € ; score 85.96/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- STO-EUR : 0.03642 € ; score 85.48/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017 | +97.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013772 | +75.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.059448 | +60.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.052846 | +54.88 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.112109 | +41.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.046033 | +38.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30472 | +33.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3714e-06 | +25.44 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.2167 | +22.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TAO-EUR | 282.28 | +22.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1142 scans ; 489229 observations ; 445 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
