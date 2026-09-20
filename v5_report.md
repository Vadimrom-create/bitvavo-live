# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T12:34:46.411367+00:00
État : OK | marchés EUR : 426 | V4 : 392 | données valides : 27
Récupération : 2026-09-20T12:34:13.046194+00:00 | âge ticker : 154.9 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/426 ; 15 min 76/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INVALID_5M
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M

## SURVEILLE

- HBAR-EUR : 0.070917 € ; score 78.17/100 ; SURVEILLE ; seuil achat non atteint
- SAGA-EUR : 0.025179 € ; score 76.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZIL-EUR : 0.0031143 € ; score 73.75/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- TAO-EUR : 217.7 € ; score 64.91/100 ; SURVEILLE ; STABILITY_HOLD
- XRP-EUR : 1.19501 € ; score 56.55/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.003628 | +77.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.000735 | +22.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENSO-EUR | 0.9787 | +18.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZAMA-EUR | 0.077301 | +14.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.025745 | +12.52 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 8.8397 | +11.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| C-EUR | 0.066266 | +10.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.031096 | +10.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.025179 | +9.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0031143 | +9.41 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 980 scans ; 420217 observations ; 227 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
