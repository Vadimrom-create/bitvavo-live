# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:32:00.102379+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T20:31:28.874865+00:00 | âge ticker : 147.4 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAIKO-EUR : 0.0801 € ; score 92.51/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.22463 € ; score 84.23/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- SNX-EUR : 0.2231 € ; score 84.00/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AVA-EUR : 0.22965 € ; score 83.34/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PYTH-EUR : 0.059463 € ; score 82.02/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.41878 | +47.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0094194 | +37.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.57783 | +24.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44667 | +23.75 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 76.31 | +22.98 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.094858 | +21.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.16803 | +20.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.01623 | +19.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.036899 | +18.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.100654 | +17.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1386 scans ; 593190 observations ; 759 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
