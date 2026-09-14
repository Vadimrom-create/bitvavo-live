# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T21:22:52.925836+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 6
Récupération : 2026-09-14T21:22:18.253843+00:00 | âge ticker : 151.6 s | durée : 154.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 65/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 204.18 € ; score 73.94/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 6.6362 € ; score 69.15/100 ; SURVEILLE ; STABILITY_HOLD
- HBAR-EUR : 0.068193 € ; score 67.14/100 ; SURVEILLE ; STABILITY_HOLD
- ETH-EUR : 2215.34 € ; score 66.78/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.025103 | +44.94 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.28121 | +40.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0527921 | +29.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14972 | +25.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| BOB-EUR | 0.0044804 | +18.91 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MTL-EUR | 0.27699 | +17.76 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0867 | +12.62 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RED-EUR | 0.12279 | +10.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.016141 | +9.39 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SENT-EUR | 0.013529 | +9.29 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 502 scans ; 215384 observations ; 86 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
