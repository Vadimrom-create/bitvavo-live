# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T01:48:10.402721+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T01:47:36.893319+00:00 | âge ticker : 149.0 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TIA-EUR : 0.43097 € ; score 91.97/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 11.7668 € ; score 91.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZBT-EUR : 0.07719 € ; score 87.40/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- FARTCOIN-EUR : 0.16267 € ; score 84.81/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.27008 € ; score 83.43/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.063386 | +52.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.46269 | +28.65 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 79.002 | +28.49 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.621 | +26.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.095561 | +22.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DYM-EUR | 0.018749 | +19.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.036502 | +18.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021139 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0082086 | +16.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 63.279 | +16.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1407 scans ; 602157 observations ; 792 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
