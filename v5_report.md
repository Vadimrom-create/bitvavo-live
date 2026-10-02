# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T07:55:38.862752+00:00
État : OK | marchés EUR : 430 | V4 : 388 | données valides : 430
Récupération : 2026-10-02T07:55:07.510921+00:00 | âge ticker : 150.1 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BABY-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- DYDX-EUR : 0.13559 € ; score 87.98/100 ; SURVEILLE ; SPREAD_RISK
- DOT-EUR : 1.0878 € ; score 87.90/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ACH-EUR : 0.0056066 € ; score 87.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BABY-EUR : 0.012328 € ; score 87.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.007834 € ; score 86.14/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00066691 | +157.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.53073 | +44.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.053367 | +38.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.11354 | +32.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.02632 | +15.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.090702 | +15.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 162.85 | +11.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.011919 | +11.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.8312 | +11.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.012994 | +11.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1965 scans ; 841028 observations ; 1539 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
