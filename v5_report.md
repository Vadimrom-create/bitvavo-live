# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T02:49:03.138191+00:00
État : OK | marchés EUR : 430 | V4 : 376 | données valides : 6
Récupération : 2026-09-17T02:48:30.022072+00:00 | âge ticker : 151.6 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 19/430 ; 15 min 38/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NEAR-EUR : CHASE_RISK, STALE_DAILY_PROFILE

## SURVEILLE

- UNI-EUR : 5.8508 € ; score 75.64/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 195.44 € ; score 74.23/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 69.148 € ; score 69.76/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.0175e-06 € ; score 68.23/100 ; SURVEILLE ; STABILITY_HOLD
- SUI-EUR : 0.62659 € ; score 66.34/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.136712 | +57.14 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LSK-EUR | 0.44804 | +32.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FOLD-EUR | 0.055215 | +24.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IOST-EUR | 0.0008023 | +24.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.004098 | +17.79 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HNT-EUR | 0.40969 | +17.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.1306 | +16.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.26323 | +16.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.111654 | +14.95 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOMI-EUR | 0.1506 | +14.92 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 679 scans ; 291364 observations ; 112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
