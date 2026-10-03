# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T08:58:31.299023+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T08:57:59.807861+00:00 | âge ticker : 145.3 s | durée : 146.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- UNI-EUR : 8.2321 € ; score 88.58/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.129643 € ; score 86.80/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.011874 € ; score 86.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZRO-EUR : 1.6361 € ; score 86.66/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.035995 € ; score 86.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.065404 | +19.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065522 | +13.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 235.123 | +12.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.006115 | +11.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMX-EUR | 0.17238 | +10.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006088 | +9.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.167977 | +8.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008316 | +7.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDP-EUR | 0.018832 | +6.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.21366 | +6.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2039 scans ; 872600 observations ; 1607 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
