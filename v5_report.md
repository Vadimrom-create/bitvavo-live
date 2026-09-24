# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T10:23:10.178051+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T10:22:36.848365+00:00 | âge ticker : 146.6 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- QNT-EUR : 62.491 € ; score 91.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : 0.6594 € ; score 87.12/100 ; SURVEILLE ; STABILITY_HOLD
- ARK-EUR : 0.15153 € ; score 86.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ETC-EUR : 8.1873 € ; score 83.19/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 58.765 € ; score 82.76/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.121693 | +45.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0021647 | +38.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.33456 | +20.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.0020717 | +19.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.21624 | +13.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.39027 | +11.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.29013 | +10.34 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CVC-EUR | 0.027156 | +8.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 58.765 | +7.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0155002 | +6.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1347 scans ; 576559 observations ; 711 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
