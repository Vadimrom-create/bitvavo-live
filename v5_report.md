# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T16:35:47.012392+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 8
Récupération : 2026-09-14T16:35:17.272791+00:00 | âge ticker : 145.3 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/429 ; 15 min 59/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- PEPE-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- XLM-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00059204 € ; score 81.31/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 9.9718 € ; score 79.68/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 203.65 € ; score 77.23/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0031667 € ; score 76.45/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 88.778 € ; score 65.84/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.258 | +36.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023788 | +35.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0498644 | +27.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.2775 | +16.63 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.14551 | +14.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0042865 | +13.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0201234 | +12.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RON-EUR | 0.0512 | +10.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QKC-EUR | 0.0022709 | +9.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.013443 | +9.07 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 486 scans ; 208520 observations ; 79 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
