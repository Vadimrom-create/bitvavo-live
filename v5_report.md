# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T06:17:38.415434+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-10-03T06:17:01.470969+00:00 | âge ticker : 159.1 s | durée : 159.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.4575 € ; score 85.86/100 ; SURVEILLE ; WICK_SETUP
- INIT-EUR : 0.098029 € ; score 83.23/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.50186 € ; score 81.13/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- IMX-EUR : 0.1668 € ; score 80.95/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AAVE-EUR : 159.04 € ; score 80.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.071054 | +70.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.0968 | +22.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.03156 | +16.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023554 | +13.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.005994 | +12.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14838 | +10.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHZ-EUR | 0.015878 | +9.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1201 | +8.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMX-EUR | 0.1668 | +8.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FOLD-EUR | 0.062169 | +7.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 2032 scans ; 869618 observations ; 1603 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
