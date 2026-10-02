# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T12:48:16.278020+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 426
Récupération : 2026-10-02T12:47:43.250401+00:00 | âge ticker : 150.8 s | durée : 152.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.49746 € | IGNITION | score 88.68/100 | entrée 6.50/10
  Entrée 0.49773 € ; stop 0.47401 € ; TP1 0.54517 € ; TP2 0.56889 € ; montant 220.23 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.303/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RARE-EUR : 0.015539 € ; score 90.07/100 ; SURVEILLE ; seuil achat non atteint
- IMX-EUR : 0.16448 € ; score 86.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- GMT-EUR : 0.008057 € ; score 85.39/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.6425 € ; score 84.62/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RSR-EUR : 0.00154 € ; score 83.81/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.0634 | +66.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032814 | +27.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.108679 | +22.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.094263 | +20.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SKY-EUR | 0.08292 | +19.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023485 | +17.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20244 | +16.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.15213 | +15.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MAGIC-EUR | 0.053442 | +14.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AXS-EUR | 1.1292 | +12.91 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1979 scans ; 847040 observations ; 1563 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
