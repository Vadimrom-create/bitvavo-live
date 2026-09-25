# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T05:52:26.064661+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T05:51:56.797624+00:00 | âge ticker : 149.8 s | durée : 151.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETC-EUR : 8.2904 € ; score 90.88/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.62888 € ; score 90.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- S-EUR : 0.035837 € ; score 87.87/100 ; SURVEILLE ; seuil achat non atteint
- ZBT-EUR : 0.07811 € ; score 87.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.034873 € ; score 86.77/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 86.236 | +36.56 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.66507 | +33.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.100768 | +27.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.4696 | +24.00 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038996 | +23.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.087048 | +20.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17364 | +18.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.022055 | +18.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20265 | +16.05 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0081211 | +15.16 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1421 scans ; 608135 observations ; 812 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
