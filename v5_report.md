# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T05:14:52.719418+00:00
État : OK | marchés EUR : 426 | V4 : 374 | données valides : 426
Récupération : 2026-09-21T05:14:24.867171+00:00 | âge ticker : 140.8 s | durée : 143.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WAL-EUR : 0.029611 € ; score 94.44/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0073536 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- IMX-EUR : 0.12429 € ; score 91.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KSM-EUR : 3.9438 € ; score 90.56/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DEEP-EUR : 0.016097 € ; score 86.21/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.05735 | +70.52 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0010001 | +62.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.27784 | +52.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030483 | +25.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.05519 | +25.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7786 | +24.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029097 | +22.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.2426 | +20.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.49066 | +19.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46499 | +19.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1049 scans ; 449611 observations ; 325 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
