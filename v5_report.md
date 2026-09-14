# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T13:37:52.828392+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 8
Récupération : 2026-09-14T13:37:18.407280+00:00 | âge ticker : 146.6 s | durée : 147.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/429 ; 15 min 56/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- QNT-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- DOGE-EUR : 0.072716 € ; score 83.36/100 ; SURVEILLE ; WICK_SETUP
- VTHO-EUR : 0.00059971 € ; score 82.44/100 ; SURVEILLE ; WICK_SETUP
- NEAR-EUR : 2.0947 € ; score 77.08/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- BTC-EUR : 67611 € ; score 76.53/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- PUMP-EUR : 0.0031446 € ; score 73.38/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.02451 | +42.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0573722 | +42.18 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0026891 | +26.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0045102 | +18.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.86043 | +18.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| REZ-EUR | 0.0037562 | +17.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.2232 | +16.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NPC-EUR | 0.01944 | +12.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.039132 | +9.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RON-EUR | 0.05055 | +9.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 477 scans ; 204659 observations ; 75 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
