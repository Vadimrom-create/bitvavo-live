# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T20:00:58.328965+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T20:00:27.607496+00:00 | âge ticker : 160.4 s | durée : 162.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 54.862 € ; score 92.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.5977 € ; score 92.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LPT-EUR : 1.4948 € ; score 91.48/100 ; SURVEILLE ; seuil achat non atteint
- MAGIC-EUR : 0.043815 € ; score 89.58/100 ; SURVEILLE ; STABILITY_HOLD
- FIL-EUR : 0.87554 € ; score 89.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.021067 | +41.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.0204 | +31.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 292.81 | +25.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051618 | +24.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069705 | +20.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12183 | +18.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.286676 | +16.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.48641 | +16.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GOAT-EUR | 0.018604 | +15.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TIA-EUR | 0.43422 | +15.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1212 scans ; 519049 observations ; 534 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
