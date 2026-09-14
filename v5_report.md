# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T17:47:29.387802+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 7
Récupération : 2026-09-14T17:47:01.979002+00:00 | âge ticker : 137.4 s | durée : 139.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/429 ; 15 min 69/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0005805 € ; score 78.51/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 204.02 € ; score 75.35/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- XRP-EUR : 1.2408 € ; score 73.20/100 ; SURVEILLE ; STABILITY_HOLD
- PUMP-EUR : 0.0032253 € ; score 72.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SUI-EUR : 0.63519 € ; score 67.07/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.25746 | +34.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023285 | +32.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.048945 | +21.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0024399 | +17.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27592 | +15.17 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SENT-EUR | 0.014104 | +13.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.14037 | +12.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NPC-EUR | 0.0198458 | +10.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0042442 | +10.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0333 | +9.84 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 490 scans ; 210236 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
