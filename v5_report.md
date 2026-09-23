# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T12:35:59.469138+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-23T12:34:56.749716+00:00 | âge ticker : 185.9 s | durée : 187.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.72 € ; score 85.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 54.616 € ; score 84.73/100 ; SURVEILLE ; WICK_SETUP
- INIT-EUR : 0.079729 € ; score 83.09/100 ; SURVEILLE ; seuil achat non atteint
- RE-EUR : 0.42195 € ; score 82.70/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 102.753 € ; score 82.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.0342 | +42.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.302001 | +34.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.33879 | +29.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 303.18 | +25.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.043057 | +24.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018932 | +23.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SENT-EUR | 0.020403 | +23.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2781 | +21.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.15858 | +20.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.086709 | +19.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1269 scans ; 543331 observations ; 644 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
