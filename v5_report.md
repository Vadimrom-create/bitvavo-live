# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T03:32:27.075124+00:00
État : OK | marchés EUR : 429 | V4 : 376 | données valides : 10
Récupération : 2026-09-14T03:31:55.614419+00:00 | âge ticker : 147.4 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 17/429 ; 15 min 43/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- HYPE-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NPC-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- SUI-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- XLM-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- XRP-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 203.86 € ; score 80.83/100 ; SURVEILLE ; seuil achat non atteint
- VTHO-EUR : 0.00063185 € ; score 79.05/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 9.8501 € ; score 78.65/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.69197 € ; score 76.01/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- FET-EUR : 0.14756 € ; score 74.88/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| REZ-EUR | 0.004106 | +26.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.021924 | +25.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FIL-EUR | 0.85841 | +21.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVC-EUR | 0.026394 | +21.88 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZKJ-EUR | 0.006104 | +17.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IQ-EUR | 0.0008271 | +16.04 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.3189 | +11.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 3.9864 | +9.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0184821 | +8.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| BABY-EUR | 0.010726 | +6.59 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 446 scans ; 191360 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
