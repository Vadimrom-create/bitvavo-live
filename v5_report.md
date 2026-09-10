# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-10T17:43:57.149912+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 11
Récupération : 2026-09-10T17:43:28.764750+00:00 | âge ticker : 141.7 s | durée : 142.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 41/430 ; 15 min 82/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- ETH-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NEAR-EUR : CHASE_RISK, STALE_DAILY_PROFILE
- QNT-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VET-EUR : 0.0068784 € ; score 81.81/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14131 € ; score 80.80/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.031466 € ; score 77.37/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 5.2084 € ; score 77.06/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 208.6 € ; score 75.28/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| CNPY-EUR | 0.22745 | +46.44 % | INSUFFICIENT_HISTORY |
| VTHO-EUR | 0.00052799 | +41.08 % | DETECTED_EARLY |
| NES-EUR | 0.12201 | +21.49 % | INSUFFICIENT_HISTORY |
| SAGA-EUR | 0.015327 | +21.01 % | EXCLUDED_BEFORE_MOVE |
| ETHFI-EUR | 0.61794 | +19.53 % | DETECTED_EARLY |
| UP-EUR | 0.05562 | +13.52 % | EXCLUDED_BEFORE_MOVE |
| MET-EUR | 0.19115 | +8.34 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| U-EUR | 0.0002425 | +7.87 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| PUFFER-EUR | 0.014381 | +7.10 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| CSPR-EUR | 0.0026439 | +5.05 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 150 scans ; 64312 observations ; 30 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
