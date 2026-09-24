# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T02:30:45.631962+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T02:30:21.141420+00:00 | âge ticker : 148.2 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.21201 € | IGNITION | score 85.53/100 | entrée 6.95/10
  Entrée 0.2113 € ; stop 0.20351 € ; TP1 0.22687 € ; TP2 0.23466 € ; montant 250.00 € ; risque théorique 10.93 € ; R/R net 1.52.
  Chase risk : 4.612/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 55.368 € ; score 91.55/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.20931 € ; score 90.36/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0140298 € ; score 89.89/100 ; SURVEILLE ; seuil achat non atteint
- ENS-EUR : 5.8936 € ; score 89.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MTL-EUR : 0.27894 € ; score 88.51/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.117389 | +46.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021966 | +42.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.042422 | +21.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.32282 | +16.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.0296 | +15.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3788 | +12.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018173 | +11.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0454036 | +10.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.032942 | +9.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28895 | +9.31 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1321 scans ; 565483 observations ; 678 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
