# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T05:34:37.623667+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T05:34:06.426084+00:00 | âge ticker : 151.1 s | durée : 152.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0085594 € | IGNITION | score 91.04/100 | entrée 7.45/10
  Entrée 0.0085663 € ; stop 0.0082608 € ; TP1 0.0091773 € ; TP2 0.0094828 € ; montant 250.00 € ; risque théorique 10.63 € ; R/R net 1.51.
  Chase risk : 3.533/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- UNI-EUR : 8.4897 € ; score 91.70/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.005627 € ; score 90.26/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- HBAR-EUR : 0.082288 € ; score 88.95/100 ; SURVEILLE ; seuil achat non atteint
- 2Z-EUR : 0.05203 € ; score 88.48/100 ; SURVEILLE ; SPREAD_RISK
- BOME-EUR : 0.0009221 € ; score 87.80/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016768 | +114.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.074638 | +65.82 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.23309 | +32.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78273 | +25.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23924 | +23.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.021445 | +18.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.065021 | +17.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.102648 | +17.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037564 | +16.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013207 | +16.04 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1506 scans ; 644430 observations ; 949 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
