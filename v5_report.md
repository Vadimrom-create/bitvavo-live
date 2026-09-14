# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T03:50:37.485263+00:00
État : OK | marchés EUR : 429 | V4 : 375 | données valides : 13
Récupération : 2026-09-14T03:50:05.393581+00:00 | âge ticker : 145.8 s | durée : 147.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 19/429 ; 15 min 44/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- NPC-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00063884 € ; score 77.47/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.6999 € ; score 76.59/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- FET-EUR : 0.14668 € ; score 76.03/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- XRP-EUR : 1.18641 € ; score 75.50/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 69.028 € ; score 75.42/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| REZ-EUR | 0.0041946 | +31.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.022285 | +27.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZKJ-EUR | 0.006166 | +19.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CVC-EUR | 0.026315 | +19.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.83537 | +18.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.00082 | +15.04 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.3165 | +13.08 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.02 | +10.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0186961 | +9.39 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| BABY-EUR | 0.010805 | +7.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 447 scans ; 191789 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
