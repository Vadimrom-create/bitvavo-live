# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T00:49:39.532420+00:00
État : OK | marchés EUR : 426 | V4 : 406 | données valides : 426
Récupération : 2026-09-24T00:49:10.092113+00:00 | âge ticker : 151.7 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 54.691 € ; score 86.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.5773 € ; score 84.94/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.2943 € ; score 84.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.5278 € ; score 83.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ANIME-EUR : 0.0029156 € ; score 83.00/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11073 | +49.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021579 | +42.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.018038 | +23.54 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SAGA-EUR | 0.041256 | +18.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.062806 | +14.19 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.3383 | +11.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455622 | +10.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.3013 | +9.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.73011 | +8.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.029072 | +7.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1315 scans ; 562927 observations ; 671 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
