# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T04:58:16.143589+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T04:57:18.972945+00:00 | âge ticker : 175.6 s | durée : 176.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAO-EUR : 263.97 € ; score 91.79/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.02498 € ; score 91.60/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 7.0702 € ; score 91.55/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.0245 € ; score 90.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ARKM-EUR : 0.11687 € ; score 89.58/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 85.333 | +34.68 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.65883 | +32.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.100833 | +26.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46861 | +25.27 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038843 | +23.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08835 | +22.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XAI-EUR | 0.0083849 | +18.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.20164 | +15.73 % | DETECTED_EARLY | NONE | NONE |
| DBR-EUR | 0.021807 | +15.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TAI-EUR | 0.00406 | +14.53 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1418 scans ; 606854 observations ; 809 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
