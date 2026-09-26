# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T19:58:56.094757+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T19:58:23.086530+00:00 | âge ticker : 154.2 s | durée : 155.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MEGA-EUR : 0.03967 € ; score 89.82/100 ; SURVEILLE ; LOW_LIQUIDITY
- ZIG-EUR : 0.046643 € ; score 86.65/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- PROM-EUR : 5.5183 € ; score 84.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HNT-EUR : 0.4841 € ; score 84.11/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- EIGEN-EUR : 0.24551 € ; score 83.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018257 | +122.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006317 | +42.40 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019752 | +36.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.12018 | +36.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.221 | +27.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.043935 | +21.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.0617 | +18.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.042962 | +17.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.659 | +16.17 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.005953 | +15.84 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1558 scans ; 666634 observations ; 1045 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
