# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T07:07:55.658849+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-23T07:07:25.082205+00:00 | âge ticker : 146.2 s | durée : 147.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CROSS-EUR : 0.137435 € ; score 90.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ZORA-EUR : 0.008148 € ; score 88.42/100 ; SURVEILLE ; WICK_SETUP
- TURBO-EUR : 0.0010085 € ; score 87.54/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PUNDIX-EUR : 0.10704 € ; score 84.92/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- MEME-EUR : 0.00056218 € ; score 84.78/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.033023 | +35.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31946 | +34.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 309.84 | +33.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.088827 | +33.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019924 | +29.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.16489 | +25.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2443 | +22.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0094845 | +20.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.48 | +20.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018418 | +19.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1251 scans ; 535663 observations ; 606 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
