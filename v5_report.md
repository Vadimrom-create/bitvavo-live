# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T16:16:53.546209+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 6
Récupération : 2026-09-14T16:16:22.633220+00:00 | âge ticker : 143.8 s | durée : 145.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 31/429 ; 15 min 59/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- PEPE-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- XLM-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0005876 € ; score 82.21/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0031407 € ; score 77.52/100 ; SURVEILLE ; STABILITY_HOLD
- LINK-EUR : 9.9513 € ; score 76.05/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 88.291 € ; score 59.31/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.023672 | +34.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.24162 | +26.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0487677 | +24.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14435 | +15.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27403 | +14.58 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NPC-EUR | 0.0200026 | +13.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0042608 | +12.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0022936 | +11.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| RON-EUR | 0.051132 | +10.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| WAXP-EUR | 0.0046701 | +9.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 485 scans ; 208091 observations ; 79 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
