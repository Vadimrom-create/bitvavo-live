# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T17:43:47.726105+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T17:43:18.079274+00:00 | âge ticker : 150.4 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FIL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- DOT-EUR : 1.091 € ; score 92.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.52193 € ; score 91.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.9347 € ; score 90.93/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ACU-EUR : 0.12088 € ; score 90.82/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DOGE-EUR : 0.085024 € ; score 89.14/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.28272 | +47.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 160.08 | +47.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 1.06 | +43.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016269 | +27.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006455 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.24884 | +22.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013729 | +20.56 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.00723 | +19.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.56362 | +19.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007125 | +17.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1634 scans ; 699086 observations ; 1162 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
