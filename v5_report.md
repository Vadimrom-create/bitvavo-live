# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T18:29:48.626665+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-29T18:29:12.727772+00:00 | âge ticker : 155.1 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : VERTICAL_SHORT_TERM, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SKY-EUR : 0.076419 € ; score 85.09/100 ; SURVEILLE ; seuil achat non atteint
- RARE-EUR : 0.015147 € ; score 85.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- HUMA-EUR : 0.026254 € ; score 81.82/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0050531 € ; score 81.45/100 ; SURVEILLE ; VERTICAL_SHORT_TERM, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.33992 € ; score 80.58/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016506 | +28.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.2935 | +27.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDP-EUR | 0.021441 | +25.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SOON-EUR | 0.36098 | +23.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002113 | +20.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.094824 | +19.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NMR-EUR | 11.574 | +18.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.1487 | +13.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.059702 | +13.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.5876 | +13.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1785 scans ; 763675 observations ; 1336 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
