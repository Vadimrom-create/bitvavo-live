# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T02:59:38.652103+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T02:59:05.382523+00:00 | âge ticker : 153.2 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAS-EUR : 0.038296 € ; score 91.39/100 ; SURVEILLE ; seuil achat non atteint
- PEAQ-EUR : 0.037701 € ; score 90.90/100 ; SURVEILLE ; WICK_SETUP
- BABY-EUR : 0.012338 € ; score 90.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PIXEL-EUR : 0.0050498 € ; score 89.58/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- JUP-EUR : 0.29146 € ; score 88.47/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.37013 | +41.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.001617 | +30.17 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.0895 | +30.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 248.136 | +26.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051658 | +25.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00050296 | +22.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.64706 | +20.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.091323 | +20.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZBCN-EUR | 0.002266 | +19.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5714 | +18.73 % | DETECTED_EARLY | NONE | NONE |

Historique : 1812 scans ; 775258 observations ; 1353 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
