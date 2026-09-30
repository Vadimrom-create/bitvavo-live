# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T21:20:13.428302+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T21:19:11.110761+00:00 | âge ticker : 194.0 s | durée : 194.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 58.687 € ; score 90.87/100 ; SURVEILLE ; WICK_SETUP
- CHR-EUR : 0.019261 € ; score 87.95/100 ; SURVEILLE ; LOW_LIQUIDITY
- DEEP-EUR : 0.020325 € ; score 85.73/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- ZRO-EUR : 1.4832 € ; score 83.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- FOLD-EUR : 0.059307 € ; score 83.73/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.7289 | +59.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3505 | +46.65 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.00814 | +19.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.42808 | +17.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.069999 | +16.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0597166 | +13.82 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AUDIO-EUR | 0.015543 | +13.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.3186 | +12.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.44318 | +12.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.36586 | +11.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1864 scans ; 797598 observations ; 1422 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
