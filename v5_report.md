# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T14:56:12.448162+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-01T14:55:36.509125+00:00 | âge ticker : 154.7 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GRAM-EUR : 1.3481 € ; score 89.38/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.20765 € ; score 88.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- YFI-EUR : 2174.4 € ; score 83.42/100 ; SURVEILLE ; SPREAD_RISK
- AAVE-EUR : 147.06 € ; score 82.49/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.43657 € ; score 82.21/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.0005744 | +119.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.2976 | +60.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.073864 | +30.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.4227 | +29.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ALICE-EUR | 0.17423 | +20.81 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYN-EUR | 0.170768 | +16.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028279 | +15.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.46841 | +15.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.138532 | +13.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33969 | +13.06 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1914 scans ; 819098 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
