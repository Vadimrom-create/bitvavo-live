# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T20:22:14.172121+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 33
Récupération : 2026-09-19T20:21:43.647456+00:00 | âge ticker : 145.7 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 33/427 ; 15 min 87/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INVALID_5M
- SEI-EUR : INVALID_15M, INVALID_5M
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUI-EUR : 0.75842 € ; score 90.41/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 79.939 € ; score 79.57/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.36731 € ; score 75.70/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- PEPE-EUR : 3.6613e-06 € ; score 74.63/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SOL-EUR : 96.73 € ; score 74.16/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.075406 | +43.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.211879 | +40.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.45976 | +38.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.32091 | +30.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0085181 | +29.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0025553 | +28.72 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17982 | +22.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.070657 | +20.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| INJ-EUR | 6.8432 | +19.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.451 | +17.72 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 920 scans ; 394619 observations ; 218 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
