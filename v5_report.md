# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T04:08:11.818542+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T04:07:37.527577+00:00 | âge ticker : 147.1 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ORCA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALICE-EUR : 0.15982 € ; score 90.86/100 ; SURVEILLE ; SPREAD_RISK
- YFI-EUR : 2323.3 € ; score 84.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PARTI-EUR : 0.024534 € ; score 84.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MAGIC-EUR : 0.053077 € ; score 83.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SLP-EUR : 0.00063801 € ; score 80.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.071032 | +78.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.093777 | +18.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.032076 | +18.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023239 | +14.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0059781 | +13.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BIGTIME-EUR | 0.008817 | +12.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14944 | +12.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1323 | +11.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.08815 | +10.53 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMX-EUR | 0.1701 | +10.37 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2026 scans ; 867062 observations ; 1597 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
