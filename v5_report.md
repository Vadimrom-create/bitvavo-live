# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T20:51:51.695304+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T20:51:19.909527+00:00 | âge ticker : 147.4 s | durée : 149.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- THE-EUR : 0.07265 € ; score 92.06/100 ; SURVEILLE ; seuil achat non atteint
- ETC-EUR : 8.1863 € ; score 91.33/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WCT-EUR : 0.038869 € ; score 86.96/100 ; SURVEILLE ; seuil achat non atteint
- SUSHI-EUR : 0.22678 € ; score 84.17/100 ; SURVEILLE ; seuil achat non atteint
- XAI-EUR : 0.00726 € ; score 83.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.021326 | +44.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020271 | +30.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 295.47 | +26.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051928 | +22.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0090798 | +19.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.50314 | +17.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12091 | +17.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.302441 | +17.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068457 | +15.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TIA-EUR | 0.43471 | +15.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1215 scans ; 520327 observations ; 535 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
