# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T22:40:32.458886+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T22:39:59.394732+00:00 | âge ticker : 149.7 s | durée : 150.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CC-EUR : 0.11973 € ; score 94.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FORM-EUR : 0.28307 € ; score 92.35/100 ; SURVEILLE ; seuil achat non atteint
- A-EUR : 0.08887 € ; score 92.15/100 ; SURVEILLE ; LOW_LIQUIDITY
- POL-EUR : 0.104796 € ; score 91.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.025994 € ; score 90.56/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016266 | +102.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006867 | +54.80 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.127153 | +44.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019399 | +38.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 117.964 | +37.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063922 | +24.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043858 | +20.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006004 | +17.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.66755 | +16.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.20238 | +14.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1568 scans ; 670904 observations ; 1051 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
