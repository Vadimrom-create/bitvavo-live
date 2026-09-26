# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T07:01:54.022147+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T07:01:25.816615+00:00 | âge ticker : 149.6 s | durée : 150.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HOT-EUR : 0.00039549 € ; score 92.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.6905 € ; score 90.60/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.94911 € ; score 90.40/100 ; SURVEILLE ; WICK_SETUP
- DOT-EUR : 1.0812 € ; score 89.29/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.026761 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0014586 | +88.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018939 | +64.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24771 | +42.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.068571 | +37.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.062829 | +32.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AERO-EUR | 0.7955 | +25.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23323 | +20.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0039879 | +17.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.12031 | +17.26 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KMNO-EUR | 0.038036 | +16.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1511 scans ; 646565 observations ; 956 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
