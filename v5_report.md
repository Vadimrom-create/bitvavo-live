# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T00:43:06.622564+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 5
Récupération : 2026-09-17T00:42:37.089136+00:00 | âge ticker : 144.0 s | durée : 144.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 18/430 ; 15 min 49/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LINK-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00060597 € ; score 84.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ONDO-EUR : 0.30573 € ; score 79.46/100 ; SURVEILLE ; WICK_SETUP
- UNI-EUR : 5.8221 € ; score 73.97/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 86.275 € ; score 65.00/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.149561 | +78.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.45984 | +34.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DGB-EUR | 0.0036312 | +18.06 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.0786 | +16.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.051389 | +16.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AGI-EUR | 0.003986 | +15.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 2.3414 | +15.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.22957 | +15.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.30688 | +14.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IOST-EUR | 0.0007319 | +13.81 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 672 scans ; 288354 observations ; 112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
