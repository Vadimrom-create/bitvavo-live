# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T19:46:25.713566+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T19:45:52.193090+00:00 | âge ticker : 157.1 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 3.0216 € ; score 93.85/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.095559 € ; score 93.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.19847 € ; score 92.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DYDX-EUR : 0.12788 € ; score 91.31/100 ; SURVEILLE ; LOW_LIQUIDITY
- BRETT-EUR : 0.0051767 € ; score 91.22/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.36829 | +54.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.5607 | +49.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.42544 | +17.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.45363 | +17.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007942 | +16.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.015964 | +16.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| UP-EUR | 0.070623 | +14.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0604678 | +13.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TRAC-EUR | 0.3696 | +13.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0041972 | +12.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1859 scans ; 795448 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
