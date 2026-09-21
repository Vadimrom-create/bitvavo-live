# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:42:58.443081+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T21:42:25.321495+00:00 | âge ticker : 148.7 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GRT-EUR : 0.020365 € ; score 93.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PORTAL-EUR : 0.017151 € ; score 90.43/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENSO-EUR : 0.8835 € ; score 87.54/100 ; SURVEILLE ; seuil achat non atteint
- IO-EUR : 0.13197 € ; score 87.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOLV-EUR : 0.0036172 € ; score 86.92/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016407 | +109.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.01691 | +96.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052046 | +51.06 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31825 | +41.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.107994 | +34.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.043249 | +34.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008643 | +32.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010567 | +29.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.39056 | +24.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.026156 | +24.43 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1120 scans ; 479857 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
