# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T22:34:24.221549+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 5
Récupération : 2026-09-14T22:33:50.389305+00:00 | âge ticker : 138.4 s | durée : 139.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/429 ; 15 min 63/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00055885 € ; score 81.56/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.33622 € ; score 72.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.27168 | +37.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023373 | +36.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0546204 | +35.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.15309 | +31.94 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| BOB-EUR | 0.0046163 | +22.52 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27746 | +17.63 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0798 | +15.89 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.013911 | +15.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0042231 | +12.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0199388 | +11.82 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 506 scans ; 217100 observations ; 91 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
