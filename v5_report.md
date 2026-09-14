# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T04:26:01.013260+00:00
État : OK | marchés EUR : 429 | V4 : 374 | données valides : 7
Récupération : 2026-09-14T04:25:29.031842+00:00 | âge ticker : 150.6 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 20/429 ; 15 min 48/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- VET-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00065384 € ; score 81.00/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 2.9783e-06 € ; score 77.21/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 204.31 € ; score 74.50/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| REZ-EUR | 0.0040954 | +32.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.021864 | +25.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CVC-EUR | 0.026843 | +25.15 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MTL-EUR | 0.3345 | +20.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZKJ-EUR | 0.006234 | +19.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.83729 | +18.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.000824 | +14.43 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.0556 | +11.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0187425 | +10.25 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| BABY-EUR | 0.010971 | +9.02 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 449 scans ; 192647 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
