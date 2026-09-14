# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T19:55:50.349992+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 8
Récupération : 2026-09-14T19:55:18.814652+00:00 | âge ticker : 147.1 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/429 ; 15 min 67/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- INJ-EUR : 5.4881 € ; score 76.56/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 2.195 € ; score 76.35/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.33869 € ; score 74.96/100 ; SURVEILLE ; seuil achat non atteint
- NPC-EUR : 0.0197896 € ; score 74.45/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 6.5887 € ; score 73.80/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.26461 | +38.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023653 | +36.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.049761 | +22.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14587 | +19.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27963 | +16.20 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SENT-EUR | 0.014147 | +13.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0334 | +10.34 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NEAR-EUR | 2.195 | +9.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACX-EUR | 0.0369 | +9.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0041885 | +9.09 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 497 scans ; 213239 observations ; 81 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
