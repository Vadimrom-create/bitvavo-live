# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T09:18:50.808266+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-26T09:18:20.935756+00:00 | âge ticker : 146.8 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAO-EUR : 276.08 € ; score 92.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : 1.0513 € ; score 90.64/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENS-EUR : 6.2174 € ; score 90.11/100 ; SURVEILLE ; seuil achat non atteint
- 0G-EUR : 0.23361 € ; score 87.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HNT-EUR : 0.4474 € ; score 86.79/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017338 | +123.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019402 | +68.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.065114 | +34.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.066716 | +29.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.24184 | +24.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24573 | +21.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78145 | +18.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.097071 | +16.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.5104 | +15.46 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| KMNO-EUR | 0.03884 | +14.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1519 scans ; 649981 observations ; 967 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
