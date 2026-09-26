# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T23:29:09.342263+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T23:28:36.332925+00:00 | âge ticker : 150.7 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BAT-EUR : 0.08387 € ; score 89.55/100 ; SURVEILLE ; LOW_LIQUIDITY
- ATOM-EUR : 1.6399 € ; score 89.50/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.103838 € ; score 88.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.007722 € ; score 88.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.011447 € ; score 88.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0015471 | +85.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006736 | +51.85 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 128.743 | +47.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.126944 | +45.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018897 | +35.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063867 | +24.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.044715 | +23.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006057 | +16.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.2071 | +16.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.66251 | +15.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1571 scans ; 672185 observations ; 1054 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
