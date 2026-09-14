# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T15:56:10.151774+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 12
Récupération : 2026-09-14T15:55:39.448345+00:00 | âge ticker : 137.6 s | durée : 138.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/429 ; 15 min 60/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- SHIB-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- SOL-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00059517 € ; score 81.62/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- XLM-EUR : 0.16742 € ; score 79.53/100 ; SURVEILLE ; WICK_SETUP
- NEAR-EUR : 2.0794 € ; score 75.86/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.62806 € ; score 74.93/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14646 € ; score 74.77/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.023494 | +35.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0525409 | +34.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.23483 | +25.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14816 | +18.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27573 | +15.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| T-EUR | 0.0043127 | +14.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0198857 | +13.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0023374 | +11.83 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| WAXP-EUR | 0.004637 | +10.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| RON-EUR | 0.050837 | +10.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 484 scans ; 207662 observations ; 79 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
