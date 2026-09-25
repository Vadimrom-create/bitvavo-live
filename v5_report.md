# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T21:26:37.771465+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-25T21:26:02.971245+00:00 | âge ticker : 151.2 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ADA-EUR : 0.22237 € ; score 92.60/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEO-EUR : 2.338 € ; score 90.39/100 ; SURVEILLE ; STABILITY_HOLD
- PYTH-EUR : 0.06394 € ; score 84.30/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 62.381 € ; score 83.73/100 ; SURVEILLE ; WICK_SETUP
- ZRO-EUR : 1.4198 € ; score 83.39/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.076477 | +72.12 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RARE-EUR | 0.014783 | +28.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.21114 | +25.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.73957 | +20.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22902 | +17.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.087574 | +16.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DEEP-EUR | 0.020088 | +16.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.44833 | +14.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.063184 | +14.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.64 | +13.33 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1473 scans ; 630339 observations ; 888 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
