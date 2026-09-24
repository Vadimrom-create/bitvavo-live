# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T01:02:56.318368+00:00
État : OK | marchés EUR : 426 | V4 : 406 | données valides : 426
Récupération : 2026-09-24T01:02:27.464183+00:00 | âge ticker : 151.1 s | durée : 152.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.5773 € ; score 90.50/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZK-EUR : 0.009878 € ; score 90.25/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GRASS-EUR : 0.40135 € ; score 86.27/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.010879 € ; score 86.17/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.2782 € ; score 85.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11346 | +51.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0022463 | +48.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.017836 | +22.16 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SAGA-EUR | 0.041501 | +17.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.064479 | +17.23 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.3462 | +14.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.31212 | +13.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0458909 | +11.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.73578 | +9.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28361 | +7.64 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1316 scans ; 563353 observations ; 671 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
