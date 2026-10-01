# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T22:19:25.034645+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T22:18:50.941293+00:00 | âge ticker : 153.9 s | durée : 154.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KSM-EUR : 4.5355 € ; score 93.07/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- MIOTA-EUR : 0.049195 € ; score 91.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 152.37 € ; score 91.15/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DYM-EUR : 0.017084 € ; score 86.06/100 ; SURVEILLE ; LOW_LIQUIDITY
- EPIC-EUR : 0.48117 € ; score 85.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00070618 | +172.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.121461 | +45.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5277 | +39.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.18963 | +28.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04619 | +26.10 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.4251 | +19.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024481 | +18.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.1657 | +18.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.50172 | +16.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.024322 | +14.66 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1936 scans ; 828558 observations ; 1504 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
