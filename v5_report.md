# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T13:51:48.759928+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 426
Récupération : 2026-10-02T13:51:19.990170+00:00 | âge ticker : 149.2 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SYRUP-EUR : 0.21993 € ; score 90.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MON-EUR : 0.031453 € ; score 90.62/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEGA-EUR : 0.04406 € ; score 89.04/100 ; SURVEILLE ; seuil achat non atteint
- ARX-EUR : 0.24161 € ; score 88.15/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- BAND-EUR : 0.2052 € ; score 87.03/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.060464 | +59.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.1125 | +27.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.16562 | +27.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.030817 | +20.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023968 | +19.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.092197 | +18.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SKY-EUR | 0.081628 | +17.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.053644 | +15.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20236 | +15.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.7 | +13.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1982 scans ; 848318 observations ; 1566 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
