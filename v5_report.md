# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-10T06:01:52.084308+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 5
Récupération : 2026-09-10T06:01:23.221510+00:00 | âge ticker : 136.3 s | durée : 137.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 30/429 ; 15 min 60/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- PYTH-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- LINK-EUR : 10.2028 € ; score 85.46/100 ; SURVEILLE ; WICK_SETUP
- BTC-EUR : 67468 € ; score 81.38/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0068528 € ; score 79.39/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 5.2433 € ; score 75.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| VTHO-EUR | 0.00054766 | +41.58 % | DETECTED_EARLY |
| ARX-EUR | 0.14986 | +18.95 % | INSUFFICIENT_HISTORY |
| NES-EUR | 0.1187 | +12.89 % | INSUFFICIENT_HISTORY |
| UP-EUR | 0.057748 | +11.91 % | EXCLUDED_BEFORE_MOVE |
| PUFFER-EUR | 0.014261 | +10.93 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| LRC-EUR | 0.00812 | +10.88 % | EXCLUDED_BEFORE_MOVE |
| U-EUR | 0.000267 | +10.29 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| BTT-EUR | 2.6546e-07 | +9.97 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| REZ-EUR | 0.0030004 | +9.97 % | DETECTED_EARLY |
| COTI-EUR | 0.016119 | +9.43 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 112 scans ; 47993 observations ; 23 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
