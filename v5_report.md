# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T22:36:17.922175+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T22:35:47.909843+00:00 | âge ticker : 150.9 s | durée : 151.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25335 € | IGNITION | score 88.77/100 | entrée 6.70/10
  Entrée 0.254 € ; stop 0.24103 € ; TP1 0.27994 € ; TP2 0.29291 € ; montant 207.31 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.396/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.37667 € | IGNITION | score 82.51/100 | entrée 7.00/10
  Entrée 0.37684 € ; stop 0.36359 € ; TP1 0.40334 € ; TP2 0.41658 € ; montant 250.00 € ; risque théorique 10.51 € ; R/R net 1.50.
  Chase risk : 2.744/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SUI-EUR : 0.7867 € | IGNITION | score 81.08/100 | entrée 7.05/10
  Entrée 0.78625 € ; stop 0.75367 € ; TP1 0.85141 € ; TP2 0.88399 € ; montant 30.87 € ; risque théorique 1.49 € ; R/R net 1.57.
  Chase risk : 2.521/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ROSE-EUR : 0.006659 € ; score 90.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SKY-EUR : 0.062053 € ; score 87.18/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.022957 € ; score 87.11/100 ; SURVEILLE ; seuil achat non atteint
- ENS-EUR : 5.6934 € ; score 86.42/100 ; SURVEILLE ; STABILITY_HOLD
- CAKE-EUR : 2.2309 € ; score 85.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.030705 | +39.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24692 | +33.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0008106 | +32.49 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055151 | +25.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.035183 | +21.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49189 | +21.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028822 | +20.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6773 | +18.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.126293 | +16.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8468 | +16.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1024 scans ; 438961 observations ; 275 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
