# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T04:27:51.071180+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T04:26:55.522401+00:00 | âge ticker : 178.1 s | durée : 179.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ENA-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAS-EUR : 0.03824 € ; score 94.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COMP-EUR : 21.347 € ; score 92.80/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7552 € ; score 88.95/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.6939 € ; score 85.67/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LIGHTER-EUR : 4.2624 € ; score 85.38/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0014978 | +93.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.073608 | +67.59 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.23617 | +36.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.035262 | +30.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.78348 | +27.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23733 | +21.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013601 | +19.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.064661 | +18.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022422 | +17.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.50654 | +16.46 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1502 scans ; 642722 observations ; 945 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
