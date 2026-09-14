# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T05:21:15.545373+00:00
État : OK | marchés EUR : 429 | V4 : 373 | données valides : 4
Récupération : 2026-09-14T05:20:43.417463+00:00 | âge ticker : 146.2 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 20/429 ; 15 min 45/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00067876 € ; score 83.11/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.74999 € ; score 81.18/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- UNI-EUR : 5.4784 € ; score 75.54/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CVC-EUR | 0.028177 | +29.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| REZ-EUR | 0.0039173 | +29.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.021908 | +25.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.34046 | +20.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZKJ-EUR | 0.006122 | +18.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.82941 | +17.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.0008183 | +14.42 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9978 | +10.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BABY-EUR | 0.010998 | +9.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRC-EUR | 0.0007605 | +9.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 452 scans ; 193934 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
