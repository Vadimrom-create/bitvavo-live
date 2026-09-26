# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T13:40:50.613885+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T13:40:18.345024+00:00 | âge ticker : 147.4 s | durée : 148.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAS-EUR : 0.040201 € ; score 93.96/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12977 € ; score 93.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.23126 € ; score 93.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AKT-EUR : 0.62158 € ; score 90.33/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 5.1802e-06 € ; score 88.98/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0021557 | +162.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020598 | +71.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0005841 | +31.32 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063676 | +29.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24141 | +21.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.105801 | +21.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.6852 | +19.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PHA-EUR | 0.070522 | +14.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.79021 | +14.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.12216 | +14.13 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1535 scans ; 656813 observations ; 990 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
