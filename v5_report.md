# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T02:24:44.403676+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T02:24:14.899498+00:00 | âge ticker : 148.6 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZRO-EUR : 1.5956 € ; score 91.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IMX-EUR : 0.16196 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- UNI-EUR : 8.0749 € ; score 88.00/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RECALL-EUR : 0.042877 € ; score 87.99/100 ; SURVEILLE ; WICK_SETUP
- SKY-EUR : 0.078587 € ; score 87.92/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.061423 | +54.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.031344 | +16.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023347 | +14.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.4914 | +13.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.51099 | +12.75 % | DETECTED_EARLY | NONE | NONE |
| ATH-EUR | 0.0059284 | +12.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14911 | +11.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.087907 | +11.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.81468 | +9.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.08685 | +8.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2022 scans ; 865358 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
