# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T20:00:54.489170+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T20:00:23.034828+00:00 | âge ticker : 157.0 s | durée : 160.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GALA-EUR : 0.0020054 € ; score 92.30/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.03044 € ; score 91.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.095726 € ; score 90.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MAGIC-EUR : 0.047855 € ; score 89.16/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- WAL-EUR : 0.029572 € ; score 88.44/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.36514 | +52.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.5304 | +48.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.42334 | +17.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007807 | +15.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.015761 | +14.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BLUR-EUR | 0.019939 | +14.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0603599 | +13.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STX-EUR | 0.31856 | +12.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.43413 | +12.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.004156 | +12.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1860 scans ; 795878 observations ; 1417 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
