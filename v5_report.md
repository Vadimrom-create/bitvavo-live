# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T01:36:35.208988+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-23T01:35:37.712480+00:00 | âge ticker : 173.2 s | durée : 174.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XRP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BREV-EUR : 0.07794 € ; score 91.81/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, STABILITY_HOLD
- SHIB-EUR : 5.3725e-06 € ; score 91.55/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAIA-EUR : 0.029317 € ; score 88.30/100 ; SURVEILLE ; SPREAD_RISK
- CROSS-EUR : 0.133713 € ; score 87.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VTHO-EUR : 0.00062481 € ; score 86.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BCH-EUR | 296.87 | +28.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.078297 | +27.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.018443 | +21.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.299047 | +21.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.228 | +20.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29132 | +19.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FLOCK-EUR | 0.075844 | +18.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.49576 | +18.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MLN-EUR | 1.4298 | +17.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CHR-EUR | 0.018511 | +17.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1232 scans ; 527569 observations ; 566 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
