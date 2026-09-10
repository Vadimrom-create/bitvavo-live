# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-10T17:57:34.511113+00:00
État : OK | marchés EUR : 430 | V4 : 396 | données valides : 13
Récupération : 2026-09-10T17:57:04.560614+00:00 | âge ticker : 139.3 s | durée : 141.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 45/430 ; 15 min 84/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- ETH-EUR : STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- QNT-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- SYRUP-EUR : 0.18567 € ; score 84.38/100 ; SURVEILLE ; seuil achat non atteint
- MANA-EUR : 0.06227 € ; score 84.15/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.031742 € ; score 78.86/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0033456 € ; score 77.69/100 ; SURVEILLE ; STABILITY_HOLD
- VET-EUR : 0.0068662 € ; score 77.40/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| CNPY-EUR | 0.22732 | +46.36 % | INSUFFICIENT_HISTORY |
| VTHO-EUR | 0.00053477 | +42.92 % | DETECTED_EARLY |
| NES-EUR | 0.12521 | +23.20 % | INSUFFICIENT_HISTORY |
| ETHFI-EUR | 0.60623 | +16.54 % | DETECTED_EARLY |
| SAGA-EUR | 0.014709 | +16.13 % | EXCLUDED_BEFORE_MOVE |
| UP-EUR | 0.055563 | +13.41 % | EXCLUDED_BEFORE_MOVE |
| U-EUR | 0.0002425 | +11.65 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| PUFFER-EUR | 0.014489 | +8.33 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| MET-EUR | 0.18821 | +6.68 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| CROSS-EUR | 0.100104 | +6.12 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 151 scans ; 64742 observations ; 30 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
