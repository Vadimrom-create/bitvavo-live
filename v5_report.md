# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T10:52:33.619122+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T10:52:06.889541+00:00 | âge ticker : 141.1 s | durée : 141.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- BONK-EUR : 3.2707e-06 € ; score 92.68/100 ; SURVEILLE ; WICK_SETUP
- RED-EUR : 0.14656 € ; score 91.02/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- HBAR-EUR : 0.082252 € ; score 90.52/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0163 € ; score 89.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- VET-EUR : 0.0082489 € ; score 89.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 85.453 | +35.78 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.20534 | +34.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.66 | +30.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.48203 | +29.20 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.09947 | +28.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.054115 | +28.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.48186 | +20.88 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FET-EUR | 0.20813 | +20.06 % | DETECTED_EARLY | NONE | NONE |
| CHIP-EUR | 0.043765 | +19.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.038666 | +19.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1438 scans ; 615394 observations ; 829 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
