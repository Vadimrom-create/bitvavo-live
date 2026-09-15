# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-15T12:28:32.520440+00:00
État : OK | marchés EUR : 429 | V4 : 362 | données valides : 5
Récupération : 2026-09-15T12:28:03.285382+00:00 | âge ticker : 138.5 s | durée : 141.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/429 ; 15 min 55/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INVALID_5M, STALE_DAILY_PROFILE
- HBAR-EUR : INVALID_5M, STALE_DAILY_PROFILE
- KAS-EUR : INVALID_5M, STALE_DAILY_PROFILE
- PUMP-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- XRP-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- UNI-EUR : 5.8604 € ; score 76.59/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.17032 € ; score 73.47/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 2.9981e-06 € ; score 73.45/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- FET-EUR : 0.13752 € ; score 73.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ALIGN-EUR | 0.0074 | +46.53 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PUFFER-EUR | 0.022423 | +34.06 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.26935 | +23.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.018235 | +21.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| VTHO-EUR | 0.00070774 | +18.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ASTR-EUR | 0.0061539 | +17.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.112376 | +11.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LAPTOP-EUR | 0.20622 | +11.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.061086 | +10.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UNI-EUR | 5.8604 | +7.08 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 550 scans ; 235976 observations ; 94 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
