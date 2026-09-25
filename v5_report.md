# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T04:41:59.597911+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T04:41:30.038860+00:00 | âge ticker : 145.1 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CAKE-EUR : 2.4171 € ; score 94.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- LTC-EUR : 62.646 € ; score 89.71/100 ; SURVEILLE ; seuil achat non atteint
- TAIKO-EUR : 0.07917 € ; score 89.24/100 ; SURVEILLE ; WICK_SETUP
- RON-EUR : 0.055957 € ; score 88.35/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- INJ-EUR : 7.0809 € ; score 85.79/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 85.529 | +36.77 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.64124 | +32.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.47633 | +27.96 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.1004 | +27.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.038614 | +22.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.088502 | +22.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XAI-EUR | 0.0083 | +17.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.20175 | +16.34 % | DETECTED_EARLY | NONE | NONE |
| TAI-EUR | 0.004064 | +14.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021344 | +14.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1417 scans ; 606427 observations ; 804 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
