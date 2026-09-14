# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T17:12:03.051748+00:00
État : OK | marchés EUR : 429 | V4 : 365 | données valides : 9
Récupération : 2026-09-14T17:11:35.721925+00:00 | âge ticker : 143.8 s | durée : 145.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/429 ; 15 min 62/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- JUP-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- NEAR-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE
- SUI-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- XRP-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 203.36 € ; score 89.49/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.147 € ; score 83.65/100 ; SURVEILLE ; WICK_SETUP
- VTHO-EUR : 0.00059497 € ; score 81.52/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ETH-EUR : 2186.28 € ; score 79.40/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0032323 € ; score 79.15/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.26348 | +38.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.02324 | +32.72 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0487599 | +24.40 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.1486 | +21.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27704 | +15.80 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ZRC-EUR | 0.0008465 | +14.55 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0023253 | +12.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0042946 | +11.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.013789 | +11.17 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NPC-EUR | 0.0196623 | +10.37 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 488 scans ; 209378 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
