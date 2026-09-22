# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T12:17:17.207395+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T12:16:48.995144+00:00 | âge ticker : 144.3 s | durée : 145.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SKL-EUR : 0.0039654 € ; score 86.58/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- SOLV-EUR : 0.0035727 € ; score 84.79/100 ; SURVEILLE ; SPREAD_RISK
- MON-EUR : 0.022027 € ; score 84.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- LRC-EUR : 0.00823 € ; score 82.94/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- KAT-EUR : 0.004367 € ; score 80.03/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017304 | +96.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.001429 | +81.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.05554 | +30.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068357 | +21.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28479 | +21.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.115918 | +20.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.3796 | +16.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2627e-06 | +15.64 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.32258 | +15.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.22141 | +14.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1181 scans ; 505843 observations ; 486 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
