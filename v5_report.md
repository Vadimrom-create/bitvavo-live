# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T06:09:00.234869+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T06:08:32.050630+00:00 | âge ticker : 143.7 s | durée : 144.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TIA-EUR : 0.42672 € ; score 91.97/100 ; SURVEILLE ; seuil achat non atteint
- GRASS-EUR : 0.40612 € ; score 91.66/100 ; SURVEILLE ; seuil achat non atteint
- MOG-EUR : 1.107e-07 € ; score 89.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MORPHO-EUR : 2.46591 € ; score 89.05/100 ; SURVEILLE ; SPREAD_RISK
- ZORA-EUR : 0.007744 € ; score 88.99/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 85.367 | +35.39 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.65812 | +32.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.101815 | +28.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46966 | +23.95 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038769 | +22.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086786 | +20.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17651 | +19.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.022283 | +19.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20385 | +16.53 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.047196 | +15.82 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1422 scans ; 608562 observations ; 812 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
