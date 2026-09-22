# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T11:30:09.756974+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T11:29:37.153277+00:00 | âge ticker : 153.5 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- FIL-EUR : 0.86736 € ; score 90.05/100 ; SURVEILLE ; seuil achat non atteint
- KSM-EUR : 3.9927 € ; score 89.70/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- TWT-EUR : 0.50735 € ; score 86.86/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- ZBT-EUR : 0.075017 € ; score 86.86/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- VTHO-EUR : 0.0006081 € ; score 84.34/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0172 | +95.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014479 | +84.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.05631 | +31.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.113811 | +31.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.9158e-07 | +30.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068281 | +21.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28038 | +20.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.39374 | +19.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3136e-06 | +17.05 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.22013 | +16.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1178 scans ; 504565 observations ; 480 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
