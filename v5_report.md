# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T19:02:43.734799+00:00
État : OK | marchés EUR : 429 | V4 : 368 | données valides : 10
Récupération : 2026-09-14T19:02:14.340340+00:00 | âge ticker : 137.3 s | durée : 139.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/429 ; 15 min 69/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- DOGE-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- UNI-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- FET-EUR : 0.14823 € ; score 83.09/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.26726 € ; score 82.99/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.1076 € ; score 76.43/100 ; SURVEILLE ; STABILITY_HOLD
- NEAR-EUR : 2.2137 € ; score 76.17/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.18465 € ; score 75.21/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.023182 | +33.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.24651 | +28.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0510886 | +26.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.014734 | +18.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.1455 | +15.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.27805 | +14.03 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0499 | +11.11 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ACX-EUR | 0.0369 | +9.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 2.2137 | +8.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RON-EUR | 0.050831 | +8.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 494 scans ; 211952 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
