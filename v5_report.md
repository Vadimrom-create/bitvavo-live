# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T10:41:29.625386+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T10:40:52.473560+00:00 | âge ticker : 154.6 s | durée : 155.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CTSI-EUR : 0.024781 € ; score 87.48/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- BNB-EUR : 674.17 € ; score 85.66/100 ; SURVEILLE ; seuil achat non atteint
- ETC-EUR : 8.1474 € ; score 81.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAI-EUR : 0.003481 € ; score 80.84/100 ; SURVEILLE ; seuil achat non atteint
- STRAX-EUR : 0.009699 € ; score 80.60/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11479 | +35.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0021175 | +35.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.0021 | +22.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.33784 | +19.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21889 | +14.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.38822 | +10.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.29013 | +10.34 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CVC-EUR | 0.026723 | +7.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ACU-EUR | 0.11379 | +6.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 58.668 | +6.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1348 scans ; 576985 observations ; 711 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
