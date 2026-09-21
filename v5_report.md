# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T23:17:03.839235+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-21T23:16:34.618029+00:00 | âge ticker : 153.2 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ROSE-EUR : 0.006746 € ; score 89.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MANA-EUR : 0.074878 € ; score 89.95/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023939 € ; score 89.23/100 ; SURVEILLE ; seuil achat non atteint
- LUNA2-EUR : 0.047348 € ; score 89.11/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- CAKE-EUR : 2.2348 € ; score 88.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014544 | +87.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015239 | +78.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.124263 | +55.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052268 | +51.71 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31999 | +42.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.04425 | +35.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008667 | +35.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010773 | +30.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.027471 | +30.43 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WIF-EUR | 0.21537 | +22.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1130 scans ; 484117 observations ; 411 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
