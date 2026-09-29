# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T12:54:06.462417+00:00
État : OK | marchés EUR : 429 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T12:53:29.196163+00:00 | âge ticker : 156.4 s | durée : 157.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.4213 € ; score 89.31/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.025744 € ; score 88.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOL-EUR : 106.258 € ; score 86.03/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : 1.36845 € ; score 84.66/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : 0.0047144 € ; score 84.55/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018 | +42.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.3095 | +40.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022169 | +24.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELO-EUR | 0.099265 | +22.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.22151 | +18.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.34691 | +18.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 10.9988 | +16.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.61729 | +16.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.0747 | +15.51 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AAVE-EUR | 152.36 | +15.19 % | DETECTED_EARLY | NONE | NONE |

Historique : 1769 scans ; 756811 observations ; 1313 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
