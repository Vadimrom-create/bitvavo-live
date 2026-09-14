# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T07:24:13.412431+00:00
État : OK | marchés EUR : 429 | V4 : 372 | données valides : 9
Récupération : 2026-09-14T07:23:42.037365+00:00 | âge ticker : 144.7 s | durée : 146.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/429 ; 15 min 44/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- VET-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- W-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XLM-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00064836 € ; score 81.82/100 ; SURVEILLE ; WICK_SETUP
- NEAR-EUR : 2.0973 € ; score 76.81/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.14866 € ; score 73.85/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.18109 € ; score 73.57/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- XRP-EUR : 1.19977 € ; score 69.88/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CVC-EUR | 0.035849 | +55.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LSK-EUR | 0.78486 | +29.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| REZ-EUR | 0.0039433 | +26.89 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FIL-EUR | 0.87107 | +24.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.020502 | +19.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IQ-EUR | 0.0008377 | +17.24 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MTL-EUR | 0.31402 | +14.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MOVR-EUR | 0.7551 | +12.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9396 | +10.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.2173 | +10.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 458 scans ; 196508 observations ; 69 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
