# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T02:03:58.909654+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T02:03:29.407402+00:00 | âge ticker : 145.7 s | durée : 146.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.10284 € ; score 86.66/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.026631 € ; score 86.42/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 20 € ; score 85.72/100 ; SURVEILLE ; seuil achat non atteint
- THE-EUR : 0.0716 € ; score 85.29/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023863 € ; score 84.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017855 | +107.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013746 | +75.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.058348 | +58.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.050441 | +47.83 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.111318 | +41.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31013 | +36.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043857 | +31.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.4501e-06 | +27.55 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21553 | +23.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.0259 | +20.93 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1140 scans ; 488377 observations ; 442 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
