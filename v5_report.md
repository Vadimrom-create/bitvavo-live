# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T19:46:35.600807+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T19:45:36.052484+00:00 | âge ticker : 183.8 s | durée : 184.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NPC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ATH-EUR : 0.005615 € ; score 93.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- COMP-EUR : 21.019 € ; score 89.27/100 ; SURVEILLE ; seuil achat non atteint
- TURBO-EUR : 0.0009294 € ; score 88.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- NPC-EUR : 0.020747 € ; score 85.90/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- IO-EUR : 0.148 € ; score 85.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017783 | +119.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006233 | +40.51 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.120416 | +36.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019817 | +36.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 107.155 | +24.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.044263 | +23.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062128 | +19.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.042884 | +17.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005992 | +17.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.74639 | +15.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1557 scans ; 666207 observations ; 1042 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
