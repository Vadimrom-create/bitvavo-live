# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T05:50:40.229749+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-23T05:50:10.045239+00:00 | âge ticker : 146.7 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.4054 € ; score 91.32/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BICO-EUR : 0.019847 € ; score 91.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HMSTR-EUR : 0.00016263 € ; score 88.70/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- YGG-EUR : 0.024811 € ; score 88.64/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 132.16 € ; score 88.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.092383 | +49.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.032722 | +32.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31345 | +31.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 296.88 | +28.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.309082 | +27.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.47893 | +25.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.019484 | +25.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.2347 | +20.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.1596 | +20.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.020344 | +20.28 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1247 scans ; 533959 observations ; 600 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
