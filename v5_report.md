# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T23:48:21.777192+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T23:47:22.909927+00:00 | âge ticker : 176.9 s | durée : 177.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AERO-EUR : 0.61195 € ; score 92.57/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.20376 € ; score 89.28/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AVNT-EUR : 0.10106 € ; score 88.99/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0038124 € ; score 87.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 2.9187e-06 € ; score 86.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0151 | +75.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.00137 | +74.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.123623 | +56.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.04868 | +41.29 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SWELL-EUR | 0.0008976 | +40.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.3042 | +35.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010811 | +33.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043073 | +31.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.02632 | +24.96 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WIF-EUR | 0.2123 | +20.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1132 scans ; 484969 observations ; 412 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
