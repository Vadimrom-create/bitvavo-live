# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-13T14:17:51.159337+00:00
État : OK | marchés EUR : 429 | V4 : 364 | données valides : 4
Récupération : 2026-09-13T14:17:20.071885+00:00 | âge ticker : 146.2 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/429 ; 15 min 61/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ONDO-EUR : 0.30047 € ; score 85.40/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 204.55 € ; score 84.15/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 67.401 € ; score 80.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.77029 | +278.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.036505 | +92.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14059 | +36.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUNDIX-EUR | 0.11264 | +29.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| POWR-EUR | 0.056435 | +22.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.00070729 | +16.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLM-EUR | 0.11136 | +16.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.033959 | +14.94 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRAX-EUR | 0.010128 | +14.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| REZ-EUR | 0.0033058 | +12.32 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 397 scans ; 170339 observations ; 57 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
