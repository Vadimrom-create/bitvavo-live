# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T22:44:25.655276+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T22:43:54.699594+00:00 | âge ticker : 152.0 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DOT-EUR : 1.0581 € ; score 90.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.8075 € ; score 89.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LIGHTER-EUR : 4.2914 € ; score 89.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AEVO-EUR : 0.022405 € ; score 89.05/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK
- NEO-EUR : 2.3157 € ; score 88.57/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020039 | +34.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.054365 | +30.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.305957 | +29.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.019754 | +27.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 296.06 | +25.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.076552 | +19.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12236 | +17.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2117 | +17.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0088423 | +15.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GOAT-EUR | 0.018404 | +15.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1222 scans ; 523309 observations ; 548 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
