# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T22:16:05.548252+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 6
Récupération : 2026-09-14T22:15:31.687550+00:00 | âge ticker : 147.3 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/429 ; 15 min 64/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0005535 € ; score 80.06/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14604 € ; score 73.35/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.024211 | +40.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.27186 | +37.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0545572 | +35.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14981 | +27.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| BOB-EUR | 0.0045368 | +20.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27746 | +17.96 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0913 | +15.69 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.013926 | +15.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0042641 | +14.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.016481 | +13.62 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 505 scans ; 216671 observations ; 87 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
