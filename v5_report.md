# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T09:22:40.103280+00:00
État : OK | marchés EUR : 429 | V4 : 370 | données valides : 6
Récupération : 2026-09-14T09:22:03.752096+00:00 | âge ticker : 148.3 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 47/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00065815 € ; score 83.00/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 2.0832 € ; score 75.38/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.62694 € ; score 73.54/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- TAO-EUR : 203.12 € ; score 70.09/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.024614 | +43.79 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CVC-EUR | 0.031999 | +42.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| REZ-EUR | 0.0042329 | +28.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.8712 | +23.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.85152 | +18.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.0008245 | +13.91 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.31537 | +13.26 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| T-EUR | 0.0041954 | +13.14 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| LIGHTER-EUR | 4.0132 | +12.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.21631 | +11.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 464 scans ; 199082 observations ; 69 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
