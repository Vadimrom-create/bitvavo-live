# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T19:04:00.480631+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T19:03:28.136679+00:00 | âge ticker : 156.4 s | durée : 157.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BREV-EUR : 0.07821 € ; score 92.63/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ICP-EUR : 2.5892 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.007455 € ; score 90.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ANIME-EUR : 0.0030597 € ; score 89.75/100 ; SURVEILLE ; WICK_SETUP
- TURBO-EUR : 0.0009398 € ; score 89.41/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.02248 | +52.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.021084 | +35.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 297.92 | +29.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.071416 | +26.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051118 | +23.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GOAT-EUR | 0.018914 | +18.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12095 | +17.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.47236 | +17.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MLN-EUR | 1.4201 | +16.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.37453 | +16.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1207 scans ; 516919 observations ; 534 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
