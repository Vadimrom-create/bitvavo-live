# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T09:19:45.161623+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T09:19:15.570254+00:00 | âge ticker : 143.5 s | durée : 144.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.51776 € | IGNITION | score 79.72/100 | entrée 6.40/10
  Entrée 1.52553 € ; stop 1.46442 € ; TP1 1.64775 € ; TP2 1.70886 € ; montant 250.00 € ; risque théorique 11.73 € ; R/R net 1.55.
  Chase risk : 3.51/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAKE-EUR : 2.4216 € ; score 90.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FLOKI-EUR : 2.5426e-05 € ; score 90.04/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.24591 € ; score 89.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RSR-EUR : 0.0015639 € ; score 89.05/100 ; SURVEILLE ; seuil achat non atteint
- EDEN-EUR : 0.0548 € ; score 87.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 155.649 | +68.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008632 | +47.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.27 | +44.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006041 | +32.89 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013716 | +23.62 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.006273 | +23.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.00665 | +21.22 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| TREAD-EUR | 0.85423 | +19.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.1135 | +15.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRIA-EUR | 0.004155 | +15.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1604 scans ; 686276 observations ; 1103 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
