# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T12:15:33.783578+00:00
État : OK | marchés EUR : 430 | V4 : 378 | données valides : 5
Récupération : 2026-09-17T12:15:06.182948+00:00 | âge ticker : 142.4 s | durée : 143.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/430 ; 15 min 61/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- FET-EUR : INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE

## SURVEILLE

- LINK-EUR : 9.7683 € ; score 80.46/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 197.74 € ; score 77.19/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 69.694 € ; score 75.73/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.070743 € ; score 75.62/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.262 | +89.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QUID-EUR | 0.062481 | +25.59 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| FOLD-EUR | 0.058739 | +18.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| GLMR-EUR | 0.005519 | +17.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.5092 | +17.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.024082 | +17.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DGB-EUR | 0.003794 | +16.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.2548 | +14.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HNT-EUR | 0.39942 | +14.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| USELESS-EUR | 0.227261 | +12.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 710 scans ; 304694 observations ; 123 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
