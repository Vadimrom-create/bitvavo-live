# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T00:21:02.207309+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 4
Récupération : 2026-09-17T00:20:32.404132+00:00 | âge ticker : 144.8 s | durée : 145.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 18/430 ; 15 min 50/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- JUP-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LINK-EUR : STALE_DAILY_PROFILE
- NPC-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ONDO-EUR : 0.30835 € ; score 82.70/100 ; SURVEILLE ; WICK_SETUP
- VTHO-EUR : 0.00059394 € ; score 80.39/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 86.327 € ; score 65.65/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.154888 | +86.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.43876 | +44.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FOLD-EUR | 0.053148 | +20.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.0731 | +17.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HNT-EUR | 0.41814 | +16.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DGB-EUR | 0.0035451 | +15.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AGI-EUR | 0.003985 | +15.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 2.33 | +14.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.2264 | +14.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.08917 | +12.74 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 671 scans ; 287924 observations ; 112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
