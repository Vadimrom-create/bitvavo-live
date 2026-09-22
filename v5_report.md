# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T20:36:39.834855+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T20:36:06.993413+00:00 | âge ticker : 147.7 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CHILLGUY-EUR : 0.012384 € ; score 89.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.65321 € ; score 88.78/100 ; SURVEILLE ; WICK_SETUP
- PLUME-EUR : 0.0140677 € ; score 88.05/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.027091 € ; score 87.25/100 ; SURVEILLE ; seuil achat non atteint
- FLR-EUR : 0.0061866 € ; score 86.91/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.021435 | +44.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01992 | +28.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 298.67 | +28.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051896 | +25.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0090408 | +18.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12023 | +17.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.303158 | +16.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.197 | +16.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.067981 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.49678 | +16.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1214 scans ; 519901 observations ; 535 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
