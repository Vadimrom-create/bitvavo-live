# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T21:20:55.313680+00:00
État : OK | marchés EUR : 430 | V4 : 378 | données valides : 430
Récupération : 2026-10-01T21:20:20.443414+00:00 | âge ticker : 157.2 s | durée : 158.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SAND-EUR : 0.039601 € ; score 89.47/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- S-EUR : 0.034409 € ; score 86.54/100 ; SURVEILLE ; seuil achat non atteint
- IOST-EUR : 0.0007759 € ; score 85.44/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- CROSS-EUR : 0.122781 € ; score 85.03/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 150.93 € ; score 84.11/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00075819 | +199.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5351 | +47.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.120196 | +45.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.19705 | +35.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04574 | +24.84 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.42973 | +22.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0725255 | +20.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.166729 | +19.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVE-EUR | 0.009386 | +18.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0023684 | +16.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1933 scans ; 827268 observations ; 1494 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
