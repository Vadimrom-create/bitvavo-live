# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T08:36:42.706341+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T08:36:11.309035+00:00 | âge ticker : 149.1 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NMR-EUR : 10.06 € ; score 91.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.21183 € ; score 90.66/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : 8.2595 € ; score 88.06/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARX-EUR : 0.25113 € ; score 87.52/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- NOM-EUR : 0.0020732 € ; score 86.96/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.065386 | +16.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 237.426 | +14.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065803 | +14.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.0060277 | +10.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDP-EUR | 0.019469 | +10.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.166492 | +7.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.079641 | +6.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16655 | +6.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.21486 | +5.85 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UP-EUR | 0.064514 | +5.71 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2038 scans ; 872174 observations ; 1607 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
