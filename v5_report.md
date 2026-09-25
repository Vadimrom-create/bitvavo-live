# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T14:41:57.014877+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T14:41:21.714637+00:00 | âge ticker : 155.0 s | durée : 155.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.28576 € ; score 93.18/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ACH-EUR : 0.0053671 € ; score 88.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.063869 € ; score 87.18/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0026949 € ; score 86.42/100 ; SURVEILLE ; STABILITY_HOLD
- CAKE-EUR : 2.4359 € ; score 84.36/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.067227 | +53.87 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.7 | +41.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19444 | +25.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021203 | +19.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.084631 | +17.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037148 | +16.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHIP-EUR | 0.04374 | +16.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 81.983 | +16.10 % | DETECTED_EARLY | NONE | NONE |
| NIL-EUR | 0.11714 | +15.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.095676 | +14.67 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1450 scans ; 620518 observations ; 859 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
