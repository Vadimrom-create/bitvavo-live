# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T17:29:48.509957+00:00
État : OK | marchés EUR : 429 | V4 : 365 | données valides : 9
Récupération : 2026-09-14T17:29:20.117853+00:00 | âge ticker : 147.7 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/429 ; 15 min 64/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- NEAR-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WAL-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.0032334 € ; score 85.67/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14735 € ; score 79.13/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.30908 € ; score 78.83/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.63416 € ; score 78.17/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2189.62 € ; score 77.60/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.26047 | +36.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023466 | +34.01 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0488748 | +23.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14602 | +18.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0023987 | +15.16 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27569 | +15.14 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| T-EUR | 0.0043072 | +12.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.013887 | +11.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRC-EUR | 0.0008225 | +11.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NPC-EUR | 0.019861 | +10.74 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 489 scans ; 209807 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
