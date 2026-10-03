# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T07:55:53.729594+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-10-03T07:55:19.700509+00:00 | âge ticker : 153.3 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.27966 € ; score 86.32/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 160.13 € ; score 86.29/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.5402 € ; score 86.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- BONK-EUR : 3.2099e-06 € ; score 85.68/100 ; SURVEILLE ; STABILITY_HOLD
- FLUID-EUR : 1.491 € ; score 84.54/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.068668 | +29.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 234.056 | +14.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065617 | +13.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.0059956 | +12.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.030814 | +9.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.099766 | +8.75 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SUPER-EUR | 0.2151 | +8.53 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMX-EUR | 0.1661 | +6.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLUID-EUR | 1.491 | +6.86 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UP-EUR | 0.064455 | +6.68 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2036 scans ; 871322 observations ; 1606 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
