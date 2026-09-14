# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T10:20:40.879706+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 12
Récupération : 2026-09-14T10:20:09.625000+00:00 | âge ticker : 139.7 s | durée : 140.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 30/429 ; 15 min 50/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- STX-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XLM-EUR : STALE_DAILY_PROFILE
- XRP-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.8167 € ; score 77.80/100 ; SURVEILLE ; SPREAD_RISK
- VTHO-EUR : 0.0006313 € ; score 76.63/100 ; SURVEILLE ; seuil achat non atteint
- NPC-EUR : 0.0183848 € ; score 74.73/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 204.65 € ; score 72.88/100 ; SURVEILLE ; STABILITY_HOLD
- DOGE-EUR : 0.073067 € ; score 67.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.026404 | +55.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CVC-EUR | 0.031748 | +42.39 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| T-EUR | 0.0046973 | +25.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.87816 | +24.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| REZ-EUR | 0.0041376 | +22.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024411 | +18.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IQ-EUR | 0.0008235 | +13.77 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9556 | +10.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.21455 | +10.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| WAXP-EUR | 0.0048269 | +10.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 467 scans ; 200369 observations ; 70 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
