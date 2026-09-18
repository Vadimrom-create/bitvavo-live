# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T16:06:35.274617+00:00
État : OK | marchés EUR : 427 | V4 : 378 | données valides : 9
Récupération : 2026-09-18T16:06:06.255569+00:00 | âge ticker : 136.4 s | durée : 137.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 48/427 ; 15 min 86/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.0037987 € ; score 85.98/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0068019 € ; score 79.06/100 ; SURVEILLE ; seuil achat non atteint
- ENA-EUR : 0.14529 € ; score 78.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- DOT-EUR : 0.9869 € ; score 76.06/100 ; SURVEILLE ; STABILITY_HOLD
- LTC-EUR : 48.745 € ; score 70.53/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0074544 | +89.55 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0044127 | +58.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.484 | +43.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.032426 | +32.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.1476 | +24.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18229 | +22.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.6411 | +21.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.028325 | +21.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044322 | +20.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.014061 | +19.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 809 scans ; 347222 observations ; 166 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
