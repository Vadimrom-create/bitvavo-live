# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T20:03:54.346179+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 35
Récupération : 2026-09-19T20:03:21.921879+00:00 | âge ticker : 151.3 s | durée : 152.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 89/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INVALID_5M
- RENDER-EUR : INVALID_5M
- SEI-EUR : WICK_SETUP, INVALID_15M, INVALID_5M

## SURVEILLE

- SUI-EUR : 0.76328 € ; score 83.27/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.36954 € ; score 82.83/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- HYPE-EUR : 80.072 € ; score 77.03/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 228.83 € ; score 74.83/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SOL-EUR : 96.69 € ; score 72.99/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.074366 | +41.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.46011 | +37.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.209195 | +37.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.008607 | +34.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0025747 | +29.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.31562 | +28.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17926 | +22.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.9188 | +20.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.070248 | +20.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CROSS-EUR | 0.138786 | +18.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 919 scans ; 394192 observations ; 218 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
