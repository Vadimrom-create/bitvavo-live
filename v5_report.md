# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T13:04:13.386320+00:00
État : OK | marchés EUR : 427 | V4 : 396 | données valides : 427
Récupération : 2026-09-25T13:03:39.666134+00:00 | âge ticker : 151.9 s | durée : 152.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZORA-EUR : 0.007836 € ; score 89.14/100 ; SURVEILLE ; LOW_LIQUIDITY
- AVNT-EUR : 0.10603 € ; score 87.80/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.011062 € ; score 85.68/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GMT-EUR : 0.007817 € ; score 85.24/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.01968 € ; score 83.59/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.062913 | +40.47 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.67374 | +33.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19681 | +28.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.100439 | +27.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 82.314 | +25.35 % | DETECTED_EARLY | NONE | NONE |
| FET-EUR | 0.21476 | +20.59 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.48108 | +20.34 % | DETECTED_EARLY | NONE | NONE |
| PIXEL-EUR | 0.0055942 | +19.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.038101 | +18.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 0.99979 | +18.14 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1445 scans ; 618383 observations ; 844 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
