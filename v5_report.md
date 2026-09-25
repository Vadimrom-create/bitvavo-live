# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T07:07:29.794503+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T07:06:32.608404+00:00 | âge ticker : 176.8 s | durée : 177.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAIKO-EUR : 0.07986 € ; score 89.65/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.7309 € ; score 87.45/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 6.9454 € ; score 87.18/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.08339 € ; score 86.74/100 ; SURVEILLE ; WICK_SETUP
- ICNT-EUR : 0.08885 € ; score 86.65/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 90.446 | +43.23 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.68865 | +38.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.104806 | +32.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48515 | +27.94 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.049979 | +22.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.087024 | +20.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.0384 | +18.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.17432 | +16.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021596 | +15.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20104 | +14.91 % | DETECTED_EARLY | NONE | NONE |

Historique : 1425 scans ; 609843 observations ; 817 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
