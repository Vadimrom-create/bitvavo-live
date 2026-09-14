# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T20:16:24.149893+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 6
Récupération : 2026-09-14T20:15:52.025540+00:00 | âge ticker : 150.0 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 67/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- VET-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- HYPE-EUR : 71.073 € ; score 79.56/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.185069 € ; score 78.06/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.34135 € ; score 77.72/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 207.71 € ; score 76.24/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.31362 € ; score 74.27/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.28065 | +44.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.024491 | +40.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0506768 | +25.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.28026 | +16.11 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.14583 | +13.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.01392 | +12.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0473 | +11.09 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| XRP-EUR | 1.27973 | +9.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| T-EUR | 0.0041675 | +9.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2013 | +9.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 498 scans ; 213668 observations ; 81 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
