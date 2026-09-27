# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T10:06:09.463602+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T10:05:35.546414+00:00 | âge ticker : 160.5 s | durée : 161.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CC-EUR : 0.1207 € ; score 93.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JTO-EUR : 0.56255 € ; score 92.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ILV-EUR : 3.5802 € ; score 87.58/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- JUP-EUR : 0.3052 € ; score 87.40/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XAI-EUR : 0.0085985 € ; score 87.23/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 152.521 | +58.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.00886 | +51.45 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 1.03 | +44.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.26513 | +41.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005979 | +27.21 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006914 | +24.46 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006259 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013433 | +21.55 % | DETECTED_EARLY | NONE | NONE |
| XVG-EUR | 0.0032416 | +18.34 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WLD-EUR | 0.49867 | +17.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1607 scans ; 687557 observations ; 1115 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
