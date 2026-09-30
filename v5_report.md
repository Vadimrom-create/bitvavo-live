# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T21:57:52.272682+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T21:57:21.131245+00:00 | âge ticker : 161.0 s | durée : 162.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZRO-EUR : 1.5115 € ; score 93.99/100 ; SURVEILLE ; WICK_SETUP
- ARX-EUR : 0.24218 € ; score 88.53/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- RENDER-EUR : 1.6793 € ; score 87.19/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 58.966 € ; score 86.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DIA-EUR : 0.14795 € ; score 84.34/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8302 | +70.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34849 | +45.81 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008234 | +21.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43229 | +19.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.01582 | +16.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.069954 | +15.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0598642 | +14.49 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STX-EUR | 0.32078 | +13.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.44758 | +13.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOMI-EUR | 0.19955 | +12.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1866 scans ; 798458 observations ; 1423 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
