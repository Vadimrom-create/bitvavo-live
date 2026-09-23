# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T02:56:15.351753+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T02:55:43.256743+00:00 | âge ticker : 145.5 s | durée : 146.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FLOKI-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLOKI-EUR : 2.668e-05 € ; score 90.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.6133 € ; score 88.14/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.089235 € ; score 88.05/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUSHI-EUR : 0.23844 € ; score 87.02/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0016919 € ; score 86.83/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.084035 | +35.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.29588 | +31.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 298.15 | +29.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2403 | +22.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29447 | +21.88 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UP-EUR | 0.064293 | +20.95 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| TREAD-EUR | 0.50552 | +20.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.15604 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.073979 | +18.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018058 | +18.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1237 scans ; 529699 observations ; 570 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
