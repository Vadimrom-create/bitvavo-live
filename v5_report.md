# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T18:01:13.144310+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T18:00:40.572268+00:00 | âge ticker : 155.5 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DATAIP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUX-EUR : 0.065516 € ; score 92.21/100 ; SURVEILLE ; seuil achat non atteint
- ATOM-EUR : 1.6457 € ; score 91.94/100 ; SURVEILLE ; WICK_SETUP
- ID-EUR : 0.03519 € ; score 87.37/100 ; SURVEILLE ; LOW_LIQUIDITY
- REZ-EUR : 0.0038688 € ; score 87.07/100 ; SURVEILLE ; WICK_SETUP
- ESP-EUR : 0.092503 € ; score 85.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016142 | +105.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.131308 | +51.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006377 | +43.01 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020411 | +41.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 108.562 | +25.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062434 | +21.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.043569 | +20.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006081 | +19.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.043776 | +19.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47013 | +16.09 % | DETECTED_EARLY | NONE | NONE |

Historique : 1551 scans ; 663645 observations ; 1017 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
