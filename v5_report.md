# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T19:50:27.678971+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-29T19:49:53.715740+00:00 | âge ticker : 156.4 s | durée : 157.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETHFI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- OP-EUR : 0.115 € ; score 86.80/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.20639 € ; score 85.88/100 ; SURVEILLE ; WICK_SETUP
- GMT-EUR : 0.007433 € ; score 85.34/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- HUMA-EUR : 0.026259 € ; score 84.45/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- COMP-EUR : 22.021 € ; score 82.74/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00176 | +40.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65905 | +29.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.36171 | +25.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.035 | +22.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.28644 | +21.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021317 | +21.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051717 | +15.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.060859 | +15.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.14984 | +14.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0087 | +13.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1789 scans ; 765391 observations ; 1338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
