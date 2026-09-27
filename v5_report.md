# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T02:30:41.078450+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T02:30:08.853905+00:00 | âge ticker : 156.3 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FIL-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.86369 € | IGNITION | score 82.21/100 | entrée 7.45/10
  Entrée 1.86765 € ; stop 1.79302 € ; TP1 2.01691 € ; TP2 2.09154 € ; montant 250.00 € ; risque théorique 11.70 € ; R/R net 1.55.
  Chase risk : 4.005/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 12.528 € ; score 94.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 1.00059 € ; score 93.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012644 € ; score 91.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- JTO-EUR : 0.54464 € ; score 89.49/100 ; SURVEILLE ; SPREAD_RISK
- ARB-EUR : 0.20007 € ; score 88.18/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 153.327 | +73.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006176 | +38.63 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017744 | +34.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006717 | +28.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.062275 | +22.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.21558 | +22.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.70483 | +21.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0012706 | +18.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.83369 | +14.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.119251 | +14.00 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1581 scans ; 676455 observations ; 1068 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
