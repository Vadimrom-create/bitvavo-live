# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T13:15:29.214734+00:00
État : OK | marchés EUR : 429 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T13:14:57.679140+00:00 | âge ticker : 152.7 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CFG-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RUNE-EUR : 0.69035 € ; score 92.92/100 ; SURVEILLE ; seuil achat non atteint
- CFG-EUR : 0.14215 € ; score 92.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.2239 € ; score 91.67/100 ; SURVEILLE ; seuil achat non atteint
- C-EUR : 0.080274 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint
- SUPER-EUR : 0.1762 € ; score 90.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017846 | +45.09 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.3039 | +38.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002216 | +23.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELO-EUR | 0.099192 | +22.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.35112 | +19.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.2218 | +17.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0995 | +17.82 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.62476 | +17.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 153.94 | +16.62 % | DETECTED_EARLY | NONE | NONE |
| EDEN-EUR | 0.058993 | +14.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1770 scans ; 757240 observations ; 1313 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
