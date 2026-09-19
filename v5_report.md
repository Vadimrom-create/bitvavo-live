# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T04:26:49.108039+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 22
Récupération : 2026-09-19T04:26:20.373512+00:00 | âge ticker : 152.9 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/427 ; 15 min 57/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- AERO-EUR : INVALID_15M, INVALID_5M
- NPC-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- ONDO-EUR : 0.35421 € ; score 76.37/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 81.383 € ; score 76.15/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 98.322 € ; score 73.97/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- NEAR-EUR : 3.2783 € ; score 73.21/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.7212 € ; score 69.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0074853 | +77.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0039568 | +38.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.0358 | +34.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.28858 | +28.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.183053 | +21.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044395 | +19.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.052473 | +17.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MORPHO-EUR | 2.37383 | +17.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.00245 | +17.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.022265 | +17.22 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 859 scans ; 368572 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
