# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T16:20:25.259996+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 33
Récupération : 2026-09-19T16:19:50.201870+00:00 | âge ticker : 154.5 s | durée : 156.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/427 ; 15 min 85/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_5M
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- SENT-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- WAL-EUR : WICK_SETUP, INVALID_5M

## SURVEILLE

- PEPE-EUR : 3.3979e-06 € ; score 92.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.99 € ; score 83.12/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 235.46 € ; score 77.82/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 97.146 € ; score 74.95/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SUI-EUR : 0.7367 € ; score 73.25/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.07226 | +40.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31867 | +33.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.2052 | +30.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.40763 | +28.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0089012 | +23.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.021934 | +21.62 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EDGE-EUR | 0.071135 | +21.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17426 | +20.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.039 | +18.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.3346 | +17.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 903 scans ; 387360 observations ; 210 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
