# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T21:38:17.622850+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T21:37:45.271954+00:00 | âge ticker : 152.7 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.82653 € | IGNITION | score 91.05/100 | entrée 7.65/10
  Entrée 1.82537 € ; stop 1.75984 € ; TP1 1.95642 € ; TP2 2.02195 € ; montant 250.00 € ; risque théorique 10.69 € ; R/R net 1.51.
  Chase risk : 2.372/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- OP-EUR : 0.12635 € ; score 93.25/100 ; SURVEILLE ; seuil achat non atteint
- VVV-EUR : 26.229 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 8.5736 € ; score 91.07/100 ; SURVEILLE ; seuil achat non atteint
- SAFE-EUR : 0.099957 € ; score 89.38/100 ; SURVEILLE ; LOW_LIQUIDITY
- WAL-EUR : 0.03231 € ; score 88.77/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001687 | +109.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0007126 | +60.64 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.130701 | +50.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019318 | +35.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.122 | +27.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061872 | +21.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043726 | +19.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00608 | +19.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.66498 | +17.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.20671 | +16.83 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1564 scans ; 669196 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
