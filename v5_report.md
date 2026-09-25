# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T19:58:53.992292+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-25T19:57:52.676032+00:00 | âge ticker : 181.2 s | durée : 182.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZORA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.063105 € ; score 94.19/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- AKT-EUR : 0.59445 € ; score 91.94/100 ; SURVEILLE ; WICK_SETUP
- STX-EUR : 0.28701 € ; score 91.94/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.41118 € ; score 90.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.22591 € ; score 89.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.073129 | +67.10 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21262 | +29.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022002 | +25.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.014398 | +25.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.48696 | +23.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.088018 | +20.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.063675 | +18.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23056 | +17.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7264 | +17.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LDO-EUR | 0.43849 | +14.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1468 scans ; 628204 observations ; 881 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
