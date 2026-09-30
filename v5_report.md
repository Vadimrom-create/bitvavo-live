# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T10:25:27.459035+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 429
Récupération : 2026-09-30T10:24:56.810562+00:00 | âge ticker : 147.8 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GRT-EUR : 0.025403 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 59.21 € ; score 88.49/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RUNE-EUR : 0.67447 € ; score 86.62/100 ; SURVEILLE ; seuil achat non atteint
- PROM-EUR : 5.6302 € ; score 85.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PENDLE-EUR : 2.0676 € ; score 85.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5957 | +80.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.32101 | +34.31 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.40127 | +32.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.09758 | +26.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008409 | +24.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.26193 | +20.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.067594 | +19.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051051 | +16.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 258.231 | +15.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.30231 | +15.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1833 scans ; 784268 observations ; 1367 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
