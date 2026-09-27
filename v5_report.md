# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T17:12:17.529541+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T17:11:22.905562+00:00 | âge ticker : 180.3 s | durée : 181.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- EIGEN-EUR : 0.23865 € ; score 93.70/100 ; SURVEILLE ; WICK_SETUP
- ORCA-EUR : 1.52198 € ; score 93.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXL-EUR : 0.048891 € ; score 93.44/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- FLUID-EUR : 1.3088 € ; score 90.08/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- XAI-EUR : 0.0084808 € ; score 90.08/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 162.62 | +51.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.28478 | +49.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.96953 | +33.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.01657 | +30.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.25325 | +25.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.00642 | +22.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.55716 | +20.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013671 | +18.63 % | DETECTED_EARLY | NONE | NONE |
| GLMR-EUR | 0.007136 | +17.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PYTH-EUR | 0.074891 | +11.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1632 scans ; 698232 observations ; 1161 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
