# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-15T00:04:32.597029+00:00
État : OK | marchés EUR : 429 | V4 : 365 | données valides : 3
Récupération : 2026-09-15T00:03:59.557687+00:00 | âge ticker : 139.0 s | durée : 139.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 16/429 ; 15 min 53/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00054851 € ; score 80.35/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.27264 | +39.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0554837 | +36.83 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023119 | +33.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.15691 | +32.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRAX-EUR | 0.010768 | +17.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.00442 | +17.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0486 | +12.66 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.013607 | +11.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.26882 | +10.68 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PUNDIX-EUR | 0.0988 | +10.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 512 scans ; 219674 observations ; 92 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
