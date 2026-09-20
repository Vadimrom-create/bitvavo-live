# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T18:54:15.814085+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 40
Récupération : 2026-09-20T18:53:43.347999+00:00 | âge ticker : 158.2 s | durée : 159.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 43/426 ; 15 min 84/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- BNB-EUR : INVALID_5M
- CAKE-EUR : INVALID_5M

## SURVEILLE

- WAL-EUR : 0.027822 € ; score 80.22/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.698 € ; score 78.06/100 ; SURVEILLE ; WICK_SETUP
- ENSO-EUR : 0.8822 € ; score 77.92/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- SOL-EUR : 95.138 € ; score 74.45/100 ; SURVEILLE ; WICK_SETUP
- RENDER-EUR : 1.4349 € ; score 73.61/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032872 | +50.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0029567 | +31.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0007906 | +28.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.22332 | +21.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.043478 | +19.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.21941 | +16.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.050284 | +15.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.048 | +14.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.725 | +14.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.032582 | +14.63 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1006 scans ; 431293 observations ; 237 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
