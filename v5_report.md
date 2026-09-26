# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T13:53:45.228187+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T13:53:14.982460+00:00 | âge ticker : 148.3 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 135.88 € ; score 92.92/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.2484e-06 € ; score 91.45/100 ; SURVEILLE ; seuil achat non atteint
- PIXEL-EUR : 0.0053236 € ; score 89.60/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- AKT-EUR : 0.62021 € ; score 89.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- WCT-EUR : 0.039063 € ; score 89.47/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020878 | +153.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020912 | +75.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.065069 | +32.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AMP-EUR | 0.0005707 | +29.18 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.111361 | +28.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.2375 | +21.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PROM-EUR | 5.6273 | +18.05 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RUNE-EUR | 0.63791 | +14.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENA-EUR | 0.2457 | +14.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7915 | +13.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1536 scans ; 657240 observations ; 990 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
