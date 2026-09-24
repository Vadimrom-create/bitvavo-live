# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T01:38:22.660108+00:00
État : OK | marchés EUR : 426 | V4 : 406 | données valides : 426
Récupération : 2026-09-24T01:37:55.054298+00:00 | âge ticker : 150.3 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KMNO-EUR : 0.031702 € ; score 88.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ONG-EUR : 0.078982 € ; score 87.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PEPE-EUR : 3.8163e-06 € ; score 85.68/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.20682 € ; score 85.57/100 ; SURVEILLE ; seuil achat non atteint
- POPCAT-EUR : 0.05 € ; score 84.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11917 | +51.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021021 | +36.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.041868 | +20.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.065 | +18.18 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CPOOL-EUR | 0.030241 | +16.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017818 | +13.74 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CAP-EUR | 0.0464848 | +12.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRIA-EUR | 0.004035 | +11.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RAY-EUR | 1.77025 | +10.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3556 | +10.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1318 scans ; 564205 observations ; 672 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
