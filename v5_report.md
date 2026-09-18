# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T22:23:45.100263+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 5
Récupération : 2026-09-18T22:23:15.364202+00:00 | âge ticker : 143.9 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 30/427 ; 15 min 83/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- PEPE-EUR : 3.3531e-06 € ; score 81.20/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 217.47 € ; score 81.16/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.34726 € ; score 76.80/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- DOGE-EUR : 0.076945 € ; score 75.59/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.004722 | +68.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038118 | +55.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0066466 | +50.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.19242 | +28.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6329 | +23.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053302 | +23.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.045331 | +23.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.243 | +23.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.028122 | +21.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.059779 | +20.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 835 scans ; 358324 observations ; 181 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
