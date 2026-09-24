# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:40:16.765908+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T20:39:47.014666+00:00 | âge ticker : 147.2 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BEAM-EUR : 0.0017715 € ; score 93.36/100 ; SURVEILLE ; SPREAD_RISK
- TAIKO-EUR : 0.08012 € ; score 88.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : 5.1033e-06 € ; score 87.95/100 ; SURVEILLE ; seuil achat non atteint
- SNX-EUR : 0.22347 € ; score 85.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LUNA-EUR : 4.825e-05 € ; score 84.91/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.41723 | +45.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0096376 | +40.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44614 | +23.28 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.56892 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 76.144 | +22.30 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.09512 | +21.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.16758 | +20.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0163226 | +19.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.036879 | +18.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10009 | +17.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1387 scans ; 593617 observations ; 759 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
