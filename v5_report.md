# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T06:05:48.959743+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-23T06:04:51.777595+00:00 | âge ticker : 171.9 s | durée : 172.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- YGG-EUR : 0.024811 € ; score 88.96/100 ; SURVEILLE ; WICK_SETUP
- ICNT-EUR : 0.0897 € ; score 85.73/100 ; SURVEILLE ; seuil achat non atteint
- ONG-EUR : 0.079725 € ; score 85.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 55.971 € ; score 83.33/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZBT-EUR : 0.081841 € ; score 82.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.09755 | +57.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 303.64 | +31.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30954 | +30.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.309423 | +29.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.031601 | +28.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019316 | +25.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.47638 | +24.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16255 | +23.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2583 | +23.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020078 | +17.96 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1248 scans ; 534385 observations ; 603 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
