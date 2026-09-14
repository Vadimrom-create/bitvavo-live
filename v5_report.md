# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T08:42:40.997169+00:00
État : OK | marchés EUR : 429 | V4 : 371 | données valides : 8
Récupération : 2026-09-14T08:42:11.001696+00:00 | âge ticker : 141.8 s | durée : 142.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 47/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SUI-EUR : STALE_DAILY_PROFILE
- TAO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- LINK-EUR : 9.8741 € ; score 86.51/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0069153 € ; score 80.16/100 ; SURVEILLE ; WICK_SETUP
- VTHO-EUR : 0.00064523 € ; score 78.17/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 2.0943 € ; score 75.50/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.3324 € ; score 74.19/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CVC-EUR | 0.033826 | +51.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.87965 | +27.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.021605 | +26.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.92329 | +26.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| REZ-EUR | 0.0041306 | +25.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.0008395 | +17.04 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.31634 | +13.34 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9676 | +12.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BABY-EUR | 0.011019 | +11.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.004124 | +11.21 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 462 scans ; 198224 observations ; 69 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
