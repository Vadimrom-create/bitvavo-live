# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T00:45:50.216812+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-23T00:45:21.439120+00:00 | âge ticker : 156.7 s | durée : 157.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.059205 € ; score 93.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.010705 € ; score 91.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENS-EUR : 6.2568 € ; score 90.93/100 ; SURVEILLE ; WICK_SETUP
- F-EUR : 0.0033052 € ; score 87.40/100 ; SURVEILLE ; LOW_LIQUIDITY
- DIA-EUR : 0.1325 € ; score 86.61/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019439 | +28.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 298.53 | +26.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.054263 | +26.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.075007 | +25.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019126 | +23.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MET-EUR | 0.29247 | +19.26 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| USELESS-EUR | 0.300631 | +19.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.075244 | +17.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.45045 | +17.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2068 | +16.66 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1229 scans ; 526291 observations ; 564 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
