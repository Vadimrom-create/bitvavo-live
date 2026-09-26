# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T00:30:19.827008+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T00:29:46.644194+00:00 | âge ticker : 157.0 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WIF-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HOT-EUR : 0.000394 € ; score 88.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- GALA-EUR : 0.0019158 € ; score 87.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- AI-EUR : 0.019047 € ; score 87.78/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- RPL-EUR : 1.8647 € ; score 86.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LINK-EUR : 12.2511 € ; score 85.87/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00149 | +88.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.075778 | +67.57 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EDGE-EUR | 0.103267 | +36.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.22356 | +26.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.06605 | +20.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.74165 | +20.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23938 | +19.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.45729 | +18.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013548 | +17.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 1.05354 | +16.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1488 scans ; 636744 observations ; 912 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
