# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T23:12:57.807113+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T23:12:27.398950+00:00 | âge ticker : 150.6 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.104108 € ; score 94.32/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11435 € ; score 94.32/100 ; SURVEILLE ; seuil achat non atteint
- ATOM-EUR : 1.633 € ; score 90.10/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 5.2158e-06 € ; score 88.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.007722 € ; score 88.81/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001545 | +88.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006791 | +53.09 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 127.928 | +47.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.124479 | +42.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018927 | +36.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.045311 | +24.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063566 | +24.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.2081 | +17.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.6696 | +16.66 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KITE-EUR | 0.13397 | +14.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1570 scans ; 671758 observations ; 1053 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
