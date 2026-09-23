# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T01:50:15.505867+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T01:49:44.214643+00:00 | âge ticker : 151.7 s | durée : 153.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SHIB-EUR : 5.3608e-06 € ; score 87.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RARE-EUR : 0.011941 € ; score 82.72/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AERO-EUR : 0.62076 € ; score 81.87/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 54.752 € ; score 81.61/100 ; SURVEILLE ; seuil achat non atteint
- F-EUR : 0.0033052 € ; score 81.53/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BCH-EUR | 298.55 | +29.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.077746 | +25.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.51837 | +23.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.076468 | +22.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.298119 | +22.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018301 | +20.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2272 | +20.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29004 | +19.26 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MLN-EUR | 1.4467 | +19.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.269714 | +17.94 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1233 scans ; 527995 observations ; 566 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
