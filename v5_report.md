# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T11:50:59.964065+00:00
État : OK | marchés EUR : 429 | V4 : 363 | données valides : 5
Récupération : 2026-09-14T11:50:27.268452+00:00 | âge ticker : 138.6 s | durée : 139.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 53/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NPC-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- XPL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00061302 € ; score 80.78/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0067264 € ; score 76.48/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.072878 € ; score 67.75/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.027843 | +63.01 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0048655 | +30.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVC-EUR | 0.029319 | +29.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FIL-EUR | 0.86878 | +22.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0492469 | +22.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| REZ-EUR | 0.0040444 | +20.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024028 | +14.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| WAXP-EUR | 0.0050075 | +11.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NPC-EUR | 0.0187555 | +11.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IQ-EUR | 0.0008071 | +11.12 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 472 scans ; 202514 observations ; 74 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
