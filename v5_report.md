# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T22:37:10.950663+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T22:36:38.456699+00:00 | âge ticker : 148.2 s | durée : 148.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 152.7 € ; score 94.93/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.108964 € ; score 91.51/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.6929 € ; score 86.43/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.049195 € ; score 84.82/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- DIA-EUR : 0.14868 € ; score 84.72/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00067063 | +159.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.122977 | +45.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5299 | +35.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.18583 | +25.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04612 | +25.16 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.42527 | +18.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024556 | +17.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.165133 | +17.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.50403 | +16.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0054356 | +14.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1937 scans ; 828988 observations ; 1506 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
