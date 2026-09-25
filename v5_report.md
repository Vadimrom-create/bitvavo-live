# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T12:00:00.103721+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 427
Récupération : 2026-09-25T11:59:32.018519+00:00 | âge ticker : 146.8 s | durée : 147.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XRP-EUR : 1.39549 € ; score 91.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.9022 € ; score 90.85/100 ; SURVEILLE ; WICK_SETUP
- HBAR-EUR : 0.083829 € ; score 90.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RSR-EUR : 0.0015321 € ; score 90.45/100 ; SURVEILLE ; seuil achat non atteint
- HOT-EUR : 0.00038775 € ; score 89.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.72846 | +46.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 85.805 | +34.58 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.20534 | +33.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.097477 | +25.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.47379 | +25.79 % | DETECTED_EARLY | NONE | NONE |
| FET-EUR | 0.21137 | +22.61 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.054416 | +21.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DEEP-EUR | 0.019925 | +21.18 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PEAQ-EUR | 0.038718 | +21.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086855 | +19.99 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1442 scans ; 617102 observations ; 833 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
