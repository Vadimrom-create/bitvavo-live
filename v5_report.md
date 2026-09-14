# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T19:23:16.365057+00:00
État : OK | marchés EUR : 429 | V4 : 369 | données valides : 11
Récupération : 2026-09-14T19:22:45.224415+00:00 | âge ticker : 140.8 s | durée : 141.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 30/429 ; 15 min 68/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- AVAX-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- DOGE-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LDO-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LINK-EUR : STALE_DAILY_PROFILE
- UNI-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- XRP-EUR : 1.27303 € ; score 84.16/100 ; SURVEILLE ; WICK_SETUP
- WLD-EUR : 0.34026 € ; score 79.00/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 89.643 € ; score 78.23/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 2.2029 € ; score 77.49/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 206.06 € ; score 75.59/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.023728 | +36.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.25687 | +34.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.050508 | +24.55 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14313 | +15.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.2774 | +13.82 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.042 | +10.91 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.013761 | +10.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2029 | +9.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACX-EUR | 0.0369 | +9.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XRP-EUR | 1.27303 | +9.03 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 495 scans ; 212381 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
