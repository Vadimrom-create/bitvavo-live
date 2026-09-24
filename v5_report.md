# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T18:59:08.856756+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T18:58:37.828111+00:00 | âge ticker : 152.2 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LIGHTER-EUR : 4.7641 € ; score 90.03/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- HYPE-EUR : 82.906 € ; score 86.71/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.9542e-06 € ; score 86.56/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.082063 € ; score 86.42/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SPK-EUR : 0.018568 € ; score 86.19/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0102093 | +47.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.36283 | +31.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0019561 | +27.58 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.61944 | +26.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44647 | +23.54 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.037 | +22.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0164832 | +21.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 74.52 | +19.54 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.091744 | +19.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.102182 | +17.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1377 scans ; 589347 observations ; 755 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
