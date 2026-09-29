# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T12:28:23.719118+00:00
État : OK | marchés EUR : 429 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T12:27:23.443646+00:00 | âge ticker : 183.2 s | durée : 184.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.4273 € ; score 92.55/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEAR-EUR : 4.2872 € ; score 90.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20616 € ; score 89.19/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.23393 € ; score 89.04/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.41953 € ; score 87.91/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018254 | +42.82 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.29621 | +34.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.099162 | +22.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.35315 | +19.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.2221 | +19.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.002129 | +18.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.61404 | +17.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 152.92 | +15.98 % | DETECTED_EARLY | NONE | NONE |
| CVX-EUR | 2.0695 | +15.61 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NMR-EUR | 10.949 | +14.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1768 scans ; 756382 observations ; 1311 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
