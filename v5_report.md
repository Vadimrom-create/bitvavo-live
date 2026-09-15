# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-15T00:32:38.505542+00:00
État : OK | marchés EUR : 429 | V4 : 365 | données valides : 3
Récupération : 2026-09-15T00:32:04.637733+00:00 | âge ticker : 141.5 s | durée : 142.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 16/429 ; 15 min 48/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00055355 € ; score 83.73/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.31534 € ; score 74.01/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CAP-EUR | 0.0556614 | +36.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.26978 | +33.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.022721 | +29.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14863 | +23.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0044934 | +18.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0603 | +12.86 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STRAX-EUR | 0.010497 | +10.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.017929 | +10.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| QKC-EUR | 0.002313 | +9.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.013585 | +9.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 513 scans ; 220103 observations ; 92 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
