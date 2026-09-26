# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T02:59:52.391771+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T02:59:20.729337+00:00 | âge ticker : 156.1 s | durée : 157.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.103947 € ; score 94.06/100 ; SURVEILLE ; WICK_SETUP
- AIXBT-EUR : 0.021062 € ; score 90.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- POL-EUR : 0.103771 € ; score 90.65/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RUNE-EUR : 0.58056 € ; score 90.17/100 ; SURVEILLE ; seuil achat non atteint
- XAI-EUR : 0.0083619 € ; score 89.83/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.074785 | +69.96 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0012993 | +68.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.23064 | +37.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7866 | +29.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.1045 | +20.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.73446 | +18.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.013311 | +17.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.021425 | +16.80 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CC-EUR | 0.11739 | +16.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SUI-EUR | 1.03024 | +16.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1497 scans ; 640587 observations ; 934 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
