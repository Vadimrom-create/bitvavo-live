# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T19:29:03.225766+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T19:28:31.520085+00:00 | âge ticker : 159.0 s | durée : 160.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RPL-EUR : 1.8366 € ; score 93.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- COMP-EUR : 20.945 € ; score 92.11/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.020019 € ; score 91.62/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.067819 € ; score 89.95/100 ; SURVEILLE ; WICK_SETUP
- APT-EUR : 0.7593 € ; score 89.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.073943 | +68.36 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21023 | +28.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014519 | +26.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.48876 | +25.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.089026 | +21.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WMTX-EUR | 0.021999 | +20.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.7402 | +19.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22464 | +16.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.062354 | +15.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.11466 | +14.98 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1466 scans ; 627350 observations ; 880 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
