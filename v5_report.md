# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T11:51:50.031003+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-01T11:51:16.188502+00:00 | âge ticker : 159.1 s | durée : 161.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WOO-EUR : 0.012122 € ; score 90.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XAI-EUR : 0.0082752 € ; score 86.82/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- LDO-EUR : 0.39539 € ; score 84.98/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 146.94 € ; score 83.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KSM-EUR : 4.6375 € ; score 83.57/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00065944 | +159.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5836 | +76.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0026534 | +30.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0664685 | +22.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028968 | +19.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33716 | +19.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.005401 | +18.94 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| JASMY-EUR | 0.0054001 | +18.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.4691 | +16.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.5966e-07 | +16.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1906 scans ; 815658 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
