# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T01:48:54.291763+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T01:48:21.667857+00:00 | âge ticker : 156.0 s | durée : 157.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- DYDX-EUR : 0.13441 € ; score 93.40/100 ; SURVEILLE ; seuil achat non atteint
- CVX-EUR : 2.0017 € ; score 88.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CAKE-EUR : 2.2218 € ; score 86.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SYN-EUR : 0.157982 € ; score 85.54/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- LDO-EUR : 0.39758 € ; score 85.13/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.059989 | +52.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0060406 | +15.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023347 | +15.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENJ-EUR | 0.030711 | +14.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.48159 | +13.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50215 | +11.72 % | DETECTED_EARLY | NONE | NONE |
| MANA-EUR | 0.088256 | +11.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.54181 | +9.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.14681 | +9.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.023027 | +8.95 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2020 scans ; 864506 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
