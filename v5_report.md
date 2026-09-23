# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T01:20:16.315340+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-23T01:19:46.874558+00:00 | âge ticker : 144.3 s | durée : 145.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BTC-EUR : 75740 € ; score 88.91/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.098751 € ; score 88.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : 1.3959 € ; score 87.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOG-EUR : 1.1012e-07 € ; score 86.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HYPE-EUR : 85.048 € ; score 86.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BCH-EUR | 301.98 | +31.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.076697 | +28.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.018599 | +23.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.301347 | +23.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29442 | +20.60 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UNI-EUR | 9.3547 | +20.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.075755 | +18.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2047 | +18.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018753 | +18.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.49576 | +18.04 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1231 scans ; 527143 observations ; 565 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
