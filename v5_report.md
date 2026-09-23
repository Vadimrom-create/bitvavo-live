# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T03:17:23.703699+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T03:16:46.962142+00:00 | âge ticker : 185.4 s | durée : 187.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- FLOKI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 55.339 € ; score 94.67/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.09021 € ; score 89.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.003502 € ; score 88.61/100 ; SURVEILLE ; seuil achat non atteint
- HOT-EUR : 0.00038868 € ; score 88.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SPK-EUR : 0.01959 € ; score 87.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.093908 | +54.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.298993 | +35.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 296.45 | +29.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.29849 | +23.09 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRO-EUR | 1.2403 | +22.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.15847 | +19.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UNI-EUR | 9.4929 | +19.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.26844 | +18.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.074444 | +17.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018429 | +17.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1238 scans ; 530125 observations ; 575 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
