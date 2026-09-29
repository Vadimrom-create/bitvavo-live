# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T16:51:50.909046+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 428
Récupération : 2026-09-29T16:50:48.176610+00:00 | âge ticker : 182.6 s | durée : 183.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUSHI-EUR : 0.23235 € ; score 85.39/100 ; SURVEILLE ; seuil achat non atteint
- DEEP-EUR : 0.01868 € ; score 82.67/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ICP-EUR : 2.9587 € ; score 82.48/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.074849 € ; score 82.16/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.29231 € ; score 79.77/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017455 | +40.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.29136 | +31.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021694 | +23.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.097603 | +23.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.35071 | +18.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.34676 | +16.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 149.05 | +15.14 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.58417 | +15.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.059453 | +13.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.1 | +13.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1780 scans ; 761530 observations ; 1331 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
