# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T09:36:13.816900+00:00
État : OK | marchés EUR : 430 | V4 : 372 | données valides : 11
Récupération : 2026-09-18T09:35:43.016495+00:00 | âge ticker : 140.1 s | durée : 142.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 43/430 ; 15 min 79/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- ONDO-EUR : CHASE_RISK, STALE_DAILY_PROFILE
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- W-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00060802 € ; score 83.72/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- VET-EUR : 0.0065944 € ; score 81.33/100 ; SURVEILLE ; WICK_SETUP
- LSK-EUR : 0.39822 € ; score 79.77/100 ; SURVEILLE ; WIDE_SPREAD_RISK, WICK_SETUP
- TAO-EUR : 216.36 € ; score 75.55/100 ; SURVEILLE ; STABILITY_HOLD
- HYPE-EUR : 77.3 € ; score 75.01/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0064625 | +76.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014649 | +39.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.4613 | +37.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.16255 | +35.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.8625 | +30.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.031696 | +29.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.1803 | +24.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.56855 | +23.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.9965 | +21.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.21374 | +17.71 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 786 scans ; 337374 observations ; 154 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
