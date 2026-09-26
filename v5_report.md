# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T04:45:18.769528+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T04:44:51.311433+00:00 | âge ticker : 144.3 s | durée : 145.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RENDER-EUR : 1.6957 € ; score 91.52/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 8.3076 € ; score 91.43/100 ; SURVEILLE ; seuil achat non atteint
- AEVO-EUR : 0.023051 € ; score 89.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- MIOTA-EUR : 0.044061 € ; score 89.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.038219 € ; score 89.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017784 | +129.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.073916 | +65.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.2255 | +32.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78218 | +26.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24267 | +23.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.033073 | +19.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.065167 | +18.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013386 | +17.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.103047 | +16.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.0375 | +16.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1503 scans ; 643149 observations ; 945 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
