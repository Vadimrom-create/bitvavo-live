# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-10T20:32:32.979095+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 6
Récupération : 2026-09-10T20:32:02.323629+00:00 | âge ticker : 139.5 s | durée : 141.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 30/430 ; 15 min 74/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- NEAR-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE

## SURVEILLE

- SUI-EUR : 0.63995 € ; score 88.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- FET-EUR : 0.14303 € ; score 79.18/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0033542 € ; score 78.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- USELESS-EUR : 0.209801 € ; score 76.88/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.19206 € ; score 76.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| VTHO-EUR | 0.00053265 | +42.57 % | INSUFFICIENT_HISTORY |
| CNPY-EUR | 0.20715 | +33.37 % | INSUFFICIENT_HISTORY |
| NES-EUR | 0.12869 | +28.78 % | EXCLUDED_BEFORE_MOVE |
| UP-EUR | 0.058484 | +21.42 % | INSUFFICIENT_HISTORY |
| SAGA-EUR | 0.015127 | +20.17 % | EXCLUDED_BEFORE_MOVE |
| ETHFI-EUR | 0.60022 | +14.89 % | DETECTED_EARLY |
| RAY-EUR | 1.21367 | +9.54 % | DETECTED_EARLY |
| EIGEN-EUR | 0.19388 | +8.25 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| MET-EUR | 0.18563 | +7.72 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| BOB-EUR | 0.00415 | +5.97 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 160 scans ; 68612 observations ; 32 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
