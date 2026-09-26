# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T13:24:57.015772+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T13:24:17.851682+00:00 | âge ticker : 156.1 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAS-EUR : 0.03989 € ; score 93.64/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.0056313 € ; score 92.97/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- AEVO-EUR : 0.023594 € ; score 87.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HUMA-EUR : 0.025079 € ; score 86.92/100 ; SURVEILLE ; SPREAD_RISK
- EIGEN-EUR : 0.23742 € ; score 85.33/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0021501 | +165.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019876 | +67.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0005807 | +31.05 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062204 | +27.27 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24286 | +21.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.10204 | +17.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.6128 | +17.62 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AERO-EUR | 0.79364 | +15.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.071132 | +13.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.6399 | +13.50 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1534 scans ; 656386 observations ; 990 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
