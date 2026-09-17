# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T12:58:09.922554+00:00
État : OK | marchés EUR : 430 | V4 : 378 | données valides : 8
Récupération : 2026-09-17T12:57:42.778142+00:00 | âge ticker : 144.9 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/430 ; 15 min 61/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- HBAR-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- SHIB-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- XRP-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- ADA-EUR : 0.17491 € ; score 78.64/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.6292 € ; score 78.35/100 ; SURVEILLE ; seuil achat non atteint
- USDC-EUR : 0.8704 € ; score 77.77/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- LSK-EUR : 0.41723 € ; score 77.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HYPE-EUR : 69.854 € ; score 76.46/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.27255 | +97.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QUID-EUR | 0.060612 | +21.84 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AGI-EUR | 0.004661 | +21.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.024487 | +19.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.5 | +16.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDEN-EUR | 0.046028 | +16.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.2801 | +16.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.0545 | +15.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DGB-EUR | 0.0036958 | +14.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.172901 | +13.78 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 712 scans ; 305554 observations ; 125 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
