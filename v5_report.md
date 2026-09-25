# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T15:54:19.368896+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T15:53:17.684747+00:00 | âge ticker : 180.5 s | durée : 181.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PROM-EUR : 4.916 € ; score 90.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.064312 € ; score 90.84/100 ; SURVEILLE ; seuil achat non atteint
- MANA-EUR : 0.08025 € ; score 85.54/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AZTEC-EUR : 0.014294 € ; score 83.41/100 ; SURVEILLE ; LOW_LIQUIDITY
- VTHO-EUR : 0.00068321 € ; score 83.37/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.063354 | +44.95 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.67641 | +37.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.015783 | +36.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19898 | +27.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086505 | +19.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.43902 | +16.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 83.443 | +15.28 % | DETECTED_EARLY | NONE | NONE |
| KMNO-EUR | 0.036798 | +14.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.020379 | +13.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.21716 | +13.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1454 scans ; 622226 observations ; 872 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
