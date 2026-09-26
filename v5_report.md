# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T17:47:48.727539+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T17:47:15.944634+00:00 | âge ticker : 148.8 s | durée : 149.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ATOM-EUR : 1.6454 € ; score 91.14/100 ; SURVEILLE ; WICK_SETUP
- GRAM-EUR : 1.3474 € ; score 90.09/100 ; SURVEILLE ; seuil achat non atteint
- FLUX-EUR : 0.065502 € ; score 88.97/100 ; SURVEILLE ; SPREAD_RISK
- ID-EUR : 0.03519 € ; score 87.37/100 ; SURVEILLE ; LOW_LIQUIDITY
- ESP-EUR : 0.0921 € ; score 85.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0015523 | +97.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.131704 | +49.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020475 | +41.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006205 | +39.16 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.785 | +26.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061838 | +20.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.043394 | +20.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00604 | +18.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.043815 | +18.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47648 | +17.99 % | DETECTED_EARLY | NONE | NONE |

Historique : 1550 scans ; 663218 observations ; 1015 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
