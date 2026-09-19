# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T20:38:09.648071+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 31
Récupération : 2026-09-19T20:37:36.200447+00:00 | âge ticker : 154.3 s | durée : 155.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/427 ; 15 min 87/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INVALID_5M
- SEI-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUI-EUR : 0.75773 € ; score 80.38/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 79.927 € ; score 77.65/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.676e-06 € ; score 76.61/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 229.5 € ; score 75.65/100 ; SURVEILLE ; STABILITY_HOLD
- ONDO-EUR : 0.36593 € ; score 74.46/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.073986 | +41.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.212345 | +38.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CELR-EUR | 0.0025984 | +30.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0083187 | +28.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31925 | +27.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.435 | +26.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.18158 | +22.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.8936 | +19.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.069445 | +18.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 8.401 | +17.25 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 921 scans ; 395046 observations ; 218 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
