# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T22:03:40.890110+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 5
Récupération : 2026-09-18T22:03:06.251525+00:00 | âge ticker : 146.3 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 84/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- ICP-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 217.41 € ; score 73.45/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.3571e-06 € ; score 58.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0044041 | +57.47 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037241 | +52.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0065533 | +40.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.19368 | +28.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2721 | +24.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APT-EUR | 0.6347 | +24.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053227 | +23.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044749 | +21.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHIP-EUR | 0.039474 | +21.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.07307 | +20.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 833 scans ; 357470 observations ; 181 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
