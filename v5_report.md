# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T12:52:38.066936+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T12:52:04.120988+00:00 | âge ticker : 158.3 s | durée : 159.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 290.63 € | IGNITION | score 85.60/100 | entrée 7.50/10
  Entrée 290.93 € ; stop 277.35 € ; TP1 318.09 € ; TP2 331.66 € ; montant 224.24 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.869/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.82279 € | IGNITION | score 76.50/100 | entrée 6.65/10
  Entrée 1.82574 € ; stop 1.7507 € ; TP1 1.97582 € ; TP2 2.05086 € ; montant 250.00 € ; risque théorique 11.99 € ; R/R net 1.56.
  Chase risk : 5.259/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.039929 € ; score 92.94/100 ; SURVEILLE ; WICK_SETUP
- VVV-EUR : 26.1626 € ; score 91.52/100 ; SURVEILLE ; WICK_SETUP
- ACH-EUR : 0.0057 € ; score 87.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- GRAM-EUR : 1.2874 € ; score 87.12/100 ; SURVEILLE ; WICK_SETUP
- MIOTA-EUR : 0.045314 € ; score 86.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020373 | +154.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020247 | +68.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006036 | +36.22 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063514 | +30.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24822 | +19.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.101802 | +19.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.532 | +17.38 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AERO-EUR | 0.80127 | +16.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24634 | +15.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.041096 | +12.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1532 scans ; 655532 observations ; 989 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
