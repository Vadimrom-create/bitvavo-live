# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T08:58:50.367956+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T08:57:54.963026+00:00 | âge ticker : 170.1 s | durée : 170.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AXS-EUR : 1.0624 € ; score 94.52/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.68577 € ; score 90.62/100 ; SURVEILLE ; WICK_SETUP
- ATOM-EUR : 1.6103 € ; score 88.72/100 ; SURVEILLE ; seuil achat non atteint
- STRK-EUR : 0.036093 € ; score 88.24/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.23244 € ; score 87.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001736 | +122.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019284 | +67.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.065099 | +34.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.06693 | +32.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24787 | +26.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24372 | +24.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.79183 | +20.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038718 | +16.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.5412 | +16.17 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EDGE-EUR | 0.096999 | +15.57 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1518 scans ; 649554 observations ; 965 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
