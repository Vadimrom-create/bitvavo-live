# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T06:27:44.391445+00:00
État : OK | marchés EUR : 430 | V4 : 375 | données valides : 5
Récupération : 2026-09-17T06:27:12.322257+00:00 | âge ticker : 144.9 s | durée : 145.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/430 ; 15 min 44/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- XPL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.4343 € ; score 75.96/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- TAO-EUR : 195.85 € ; score 72.72/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.158264 | +53.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.19708 | +46.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HNT-EUR | 0.4278 | +24.35 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QUID-EUR | 0.058673 | +19.20 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| HEI-EUR | 0.115094 | +18.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FOLD-EUR | 0.054404 | +17.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| USELESS-EUR | 0.232121 | +16.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 2.3285 | +14.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 21.491 | +14.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00415 | +14.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 691 scans ; 296524 observations ; 117 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
