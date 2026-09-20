# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T15:32:49.758089+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 33
Récupération : 2026-09-20T15:32:19.332560+00:00 | âge ticker : 150.4 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/426 ; 15 min 72/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- LTC-EUR : INVALID_5M

## SURVEILLE

- HYPE-EUR : 79.543 € ; score 78.42/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 10.6682 € ; score 74.88/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- SUI-EUR : 0.72235 € ; score 73.81/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.4336e-06 € ; score 72.30/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- TAO-EUR : 220.35 € ; score 72.23/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0034534 | +63.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.028018 | +26.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.072302 | +23.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.6711 | +18.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0007067 | +17.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.47348 | +16.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| REQ-EUR | 0.053215 | +13.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ALGO-EUR | 0.097613 | +11.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.025336 | +10.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.030503 | +9.37 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 991 scans ; 424903 observations ; 230 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
