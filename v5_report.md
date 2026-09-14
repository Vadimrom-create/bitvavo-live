# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T18:46:50.320850+00:00
État : OK | marchés EUR : 429 | V4 : 369 | données valides : 9
Récupération : 2026-09-14T18:46:22.330980+00:00 | âge ticker : 142.7 s | durée : 143.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/429 ; 15 min 68/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- ALGO-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- HYPE-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- SOL-EUR : STALE_DAILY_PROFILE
- TAO-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- LINK-EUR : 10.1326 € ; score 84.48/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.2743 € ; score 82.88/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.64255 € ; score 78.43/100 ; SURVEILLE ; WICK_SETUP
- NEAR-EUR : 2.216 € ; score 77.79/100 ; SURVEILLE ; STABILITY_HOLD
- PUMP-EUR : 0.0032391 € ; score 72.17/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.02294 | +30.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.05125 | +26.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.23588 | +24.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.015055 | +20.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.2774 | +13.77 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.14134 | +12.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PENDLE-EUR | 2.0355 | +10.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NEAR-EUR | 2.216 | +8.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NPC-EUR | 0.0198566 | +8.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0041784 | +8.83 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 493 scans ; 211523 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
