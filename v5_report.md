# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-13T12:09:34.929718+00:00
État : OK | marchés EUR : 429 | V4 : 356 | données valides : 3
Récupération : 2026-09-13T12:09:02.753705+00:00 | âge ticker : 145.4 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/429 ; 15 min 52/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- XPL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- NPC-EUR : 0.0169534 € ; score 76.95/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 200.77 € ; score 74.54/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.89518 | +381.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16399 | +62.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVC-EUR | 0.026651 | +41.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| POWR-EUR | 0.062062 | +34.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.072472 | +30.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUNDIX-EUR | 0.1065 | +25.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| VTHO-EUR | 0.00075053 | +24.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0034423 | +22.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.2772 | +20.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.16152 | +19.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 388 scans ; 166478 observations ; 57 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
