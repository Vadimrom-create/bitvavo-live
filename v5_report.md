# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T03:01:29.064755+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T03:00:55.587899+00:00 | âge ticker : 147.5 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FIL-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BIGTIME-EUR : 0.008091 € ; score 92.64/100 ; SURVEILLE ; LOW_LIQUIDITY
- JUP-EUR : 0.30074 € ; score 90.97/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SHELL-EUR : 0.02386 € ; score 90.96/100 ; SURVEILLE ; seuil achat non atteint
- STRAX-EUR : 0.010623 € ; score 89.85/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- BABY-EUR : 0.012472 € ; score 86.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 150.726 | +72.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006176 | +37.83 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.2356 | +33.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017319 | +29.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006422 | +23.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.060819 | +19.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.69238 | +18.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.042416 | +15.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.50439 | +15.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.84018 | +13.71 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1583 scans ; 677309 observations ; 1068 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
