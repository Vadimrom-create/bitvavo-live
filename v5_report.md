# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T06:00:28.617070+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T06:00:00.258795+00:00 | âge ticker : 145.3 s | durée : 145.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.4405 € ; score 92.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.3849 € ; score 90.63/100 ; SURVEILLE ; WICK_SETUP
- ACH-EUR : 0.0053977 € ; score 90.60/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- JTO-EUR : 0.49332 € ; score 89.87/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AVNT-EUR : 0.11148 € ; score 89.43/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.2567 | +48.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.3844 | +46.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0025015 | +32.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6279 | +21.08 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 250.045 | +18.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00049292 | +17.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0050574 | +16.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.30942 | +16.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.066077 | +16.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.091895 | +16.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1821 scans ; 779119 observations ; 1359 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
