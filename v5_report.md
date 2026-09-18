# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T17:11:29.527921+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 12
Récupération : 2026-09-18T17:11:00.919745+00:00 | âge ticker : 140.3 s | durée : 141.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 52/427 ; 15 min 88/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- VET-EUR : STABILITY_HOLD, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- NPC-EUR : 0.0205459 € ; score 89.74/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.5449 € ; score 89.60/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 119.61 € ; score 86.57/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.3603 € ; score 74.25/100 ; SURVEILLE ; STABILITY_HOLD
- DOGE-EUR : 0.076103 € ; score 66.31/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0074781 | +91.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0043409 | +55.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.52343 | +50.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.024574 | +37.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.065224 | +32.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.032335 | +30.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18765 | +23.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.1873 | +21.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.013317 | +18.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044847 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 813 scans ; 348930 observations ; 166 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
