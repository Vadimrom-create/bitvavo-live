# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T07:22:40.087509+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-01T07:22:05.120197+00:00 | âge ticker : 159.9 s | durée : 160.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DOT-EUR : 1.1056 € ; score 91.11/100 ; SURVEILLE ; WICK_SETUP
- KSM-EUR : 4.6902 € ; score 84.27/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MERL-EUR : 0.027938 € ; score 82.61/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 147.25 € ; score 80.63/100 ; SURVEILLE ; seuil achat non atteint
- GTC-EUR : 0.08581 € ; score 79.94/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.5969 | +67.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.362 | +51.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STX-EUR | 0.35877 | +29.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029801 | +26.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0023604 | +25.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.43249 | +23.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.48892 | +21.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICX-EUR | 0.007669 | +21.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.065097 | +21.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ESP-EUR | 0.098574 | +13.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1893 scans ; 810068 observations ; 1450 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
