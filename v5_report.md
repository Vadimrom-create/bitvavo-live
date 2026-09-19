# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T03:52:49.639918+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 20
Récupération : 2026-09-19T03:51:47.695360+00:00 | âge ticker : 179.0 s | durée : 180.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/427 ; 15 min 59/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- LTC-EUR : INVALID_5M
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAO-EUR : 224.37 € ; score 84.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.35339 € ; score 79.23/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 81.542 € ; score 78.32/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 7.84 € ; score 78.17/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.6647 € ; score 77.59/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0070508 | +68.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038761 | +44.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0037967 | +33.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.28501 | +25.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.189727 | +24.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0025148 | +20.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044395 | +19.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.052975 | +19.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.06037 | +19.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| INJ-EUR | 5.9459 | +16.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 857 scans ; 367718 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
