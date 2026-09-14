# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T04:04:28.936807+00:00
État : OK | marchés EUR : 429 | V4 : 375 | données valides : 6
Récupération : 2026-09-14T04:04:00.170191+00:00 | âge ticker : 144.9 s | durée : 145.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 19/429 ; 15 min 46/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NPC-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- UNI-EUR : 5.5242 € ; score 81.64/100 ; SURVEILLE ; WICK_SETUP
- VTHO-EUR : 0.00064124 € ; score 81.53/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 69.029 € ; score 77.55/100 ; SURVEILLE ; STABILITY_HOLD
- SUI-EUR : 0.61844 € ; score 65.14/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| REZ-EUR | 0.0041325 | +30.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.0215 | +23.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CVC-EUR | 0.026297 | +22.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZKJ-EUR | 0.006242 | +20.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.82885 | +17.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.0008277 | +15.34 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.31809 | +15.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.0009 | +10.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0186954 | +9.97 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| BABY-EUR | 0.010757 | +7.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 448 scans ; 192218 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
