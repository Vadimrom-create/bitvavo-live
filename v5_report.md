# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T07:13:40.255692+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-10-03T07:13:10.430390+00:00 | âge ticker : 153.3 s | durée : 154.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.4812 € ; score 93.57/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0059956 € ; score 93.36/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.030501 € ; score 90.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0049107 € ; score 90.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AVAX-EUR : 9.6711 € ; score 87.99/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.068389 | +44.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 237.114 | +18.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0059956 | +13.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.093587 | +12.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IMX-EUR | 0.17148 | +12.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENJ-EUR | 0.031095 | +11.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023234 | +9.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.14676 | +9.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.16895 | +9.00 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.098729 | +8.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2034 scans ; 870470 observations ; 1605 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
