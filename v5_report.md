# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T04:45:44.566715+00:00
État : OK | marchés EUR : 429 | V4 : 374 | données valides : 7
Récupération : 2026-09-14T04:45:09.745689+00:00 | âge ticker : 146.2 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 19/429 ; 15 min 46/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00066499 € ; score 82.99/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 5.5239 € ; score 78.63/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2175.12 € ; score 76.43/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.73319 € ; score 74.64/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, VERTICAL_SHORT_TERM

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| REZ-EUR | 0.0040751 | +33.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.022146 | +27.08 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.34802 | +24.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CVC-EUR | 0.026759 | +22.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.8374 | +18.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZKJ-EUR | 0.006082 | +16.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IQ-EUR | 0.0008181 | +13.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.0403 | +11.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BABY-EUR | 0.011105 | +10.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0187418 | +10.25 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 450 scans ; 193076 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
