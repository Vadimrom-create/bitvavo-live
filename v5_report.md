# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T10:31:15.238297+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-21T10:30:45.128923+00:00 | âge ticker : 152.7 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : 0.017905 € | IGNITION | score 80.70/100 | entrée 6.30/10
  Entrée 0.017935 € ; stop 0.017009 € ; TP1 0.019787 € ; TP2 0.020713 € ; montant 205.30 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.844/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ROSE-EUR : 0.006891 € ; score 91.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IOST-EUR : 0.0007765 € ; score 88.98/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- SAND-EUR : 0.036203 € ; score 87.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KSM-EUR : 4.0398 € ; score 86.58/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MANA-EUR : 0.074755 € ; score 86.58/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056537 | +72.47 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.052513 | +67.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009487 | +51.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057371 | +33.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030256 | +30.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23772 | +29.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.015975 | +25.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SEI-EUR | 0.051717 | +25.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.03159 | +24.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.03059 | +23.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1068 scans ; 457705 observations ; 338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
