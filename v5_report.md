# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T04:08:30.789693+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 20
Récupération : 2026-09-19T04:07:58.153638+00:00 | âge ticker : 159.0 s | durée : 159.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 21/427 ; 15 min 59/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- LTC-EUR : STABILITY_HOLD, INVALID_5M
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INVALID_5M

## SURVEILLE

- SUI-EUR : 0.72343 € ; score 86.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 98.447 € ; score 75.88/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 7.4089 € ; score 75.02/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 81.222 € ; score 74.89/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- ONDO-EUR : 0.35488 € ; score 74.65/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.007136 | +69.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038167 | +43.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038552 | +35.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29436 | +30.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.18653 | +23.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0025124 | +20.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.053274 | +19.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044395 | +19.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 5.9535 | +17.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MORPHO-EUR | 2.37546 | +16.95 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 858 scans ; 368145 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
