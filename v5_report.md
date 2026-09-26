# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T12:34:28.264125+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T12:33:50.414366+00:00 | âge ticker : 162.0 s | durée : 163.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 292.84 € | IGNITION | score 91.18/100 | entrée 7.70/10
  Entrée 292.81 € ; stop 277.33 € ; TP1 323.77 € ; TP2 339.25 € ; montant 201.07 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 7.08/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.82018 € | IGNITION | score 90.30/100 | entrée 7.05/10
  Entrée 1.82674 € ; stop 1.74872 € ; TP1 1.98278 € ; TP2 2.0608 € ; montant 242.13 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.563/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SPK-EUR : 0.021536 € ; score 88.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.43355 € ; score 85.43/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.4527 € ; score 85.07/100 ; SURVEILLE ; SPREAD_RISK
- EIGEN-EUR : 0.23698 € ; score 83.94/100 ; SURVEILLE ; seuil achat non atteint
- CC-EUR : 0.11917 € ; score 83.86/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.002066 | +157.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020431 | +70.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0005944 | +34.15 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063143 | +29.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24528 | +20.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PROM-EUR | 5.7147 | +20.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AERO-EUR | 0.81217 | +18.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.10014 | +17.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24624 | +17.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.070048 | +15.35 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1531 scans ; 655105 observations ; 986 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
