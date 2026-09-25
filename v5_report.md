# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T17:42:03.607423+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-25T17:41:32.753501+00:00 | âge ticker : 152.6 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : 85.857 € | IGNITION | score 74.79/100 | entrée 6.60/10
  Entrée 85.777 € ; stop 81.936 € ; TP1 93.458 € ; TP2 97.299 € ; montant 232.46 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.019/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RED-EUR : 0.15283 € ; score 93.21/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK
- GOAT-EUR : 0.01687 € ; score 90.39/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK, STABILITY_HOLD
- GALA-EUR : 0.0018556 € ; score 89.87/100 ; SURVEILLE ; WICK_SETUP
- SLP-EUR : 0.00061431 € ; score 89.12/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0081936 € ; score 88.95/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.070654 | +63.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WMTX-EUR | 0.023332 | +42.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.20306 | +28.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.48193 | +26.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014409 | +24.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74501 | +20.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22828 | +19.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086465 | +18.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.66369 | +17.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.021845 | +16.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1460 scans ; 624788 observations ; 878 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
