# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-13T18:51:40.248456+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 9
Récupération : 2026-09-13T18:51:07.287762+00:00 | âge ticker : 149.8 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/429 ; 15 min 56/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- VET-EUR : STALE_DAILY_PROFILE
- W-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- SUI-EUR : 0.62418 € ; score 81.87/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.30353 € ; score 80.17/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 9.8727 € ; score 77.50/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14831 € ; score 77.39/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 204.5 € ; score 75.76/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.84057 | +260.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.030145 | +54.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FIL-EUR | 0.85664 | +23.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.0007005 | +22.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0041428 | +19.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.12514 | +17.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0027483 | +16.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| POWR-EUR | 0.053768 | +14.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.25077 | +12.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRAX-EUR | 0.009589 | +11.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 415 scans ; 178061 observations ; 58 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
