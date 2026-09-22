# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T07:56:41.727676+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T07:56:12.130355+00:00 | âge ticker : 144.3 s | durée : 145.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PENGU-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PORTAL-EUR : SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- XLM-EUR : 0.185 € ; score 90.18/100 ; SURVEILLE ; WICK_SETUP
- IMX-EUR : 0.13061 € ; score 89.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZRO-EUR : 1.0312 € ; score 87.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PUMP-EUR : 0.003994 € ; score 87.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LUNA2-EUR : 0.046808 € ; score 85.52/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0182 | +113.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015771 | +103.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.119851 | +47.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.058589 | +43.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5022e-06 | +28.49 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.39303 | +23.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.065697 | +19.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FORM-EUR | 0.27545 | +19.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21081 | +19.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FARTCOIN-EUR | 0.1778 | +18.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1164 scans ; 498601 observations ; 468 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
