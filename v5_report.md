# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T09:23:12.527327+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T09:22:14.549060+00:00 | âge ticker : 191.9 s | durée : 192.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : 0.057987 € | IGNITION | score 77.07/100 | entrée 7.40/10
  Entrée 0.057987 € ; stop 0.05436 € ; TP1 0.065241 € ; TP2 0.068867 € ; montant 173.09 € ; risque théorique 12.00 € ; R/R net 1.70.
  Chase risk : 6.844/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BEAM-EUR : 0.00184 € ; score 87.60/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.03638 € ; score 87.52/100 ; SURVEILLE ; seuil achat non atteint
- GRT-EUR : 0.023359 € ; score 84.71/100 ; SURVEILLE ; seuil achat non atteint
- AVA-EUR : 0.23232 € ; score 83.66/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MIOTA-EUR : 0.043086 € ; score 83.63/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.72529 | +45.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 86.396 | +38.68 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.20148 | +34.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.103426 | +33.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48537 | +29.41 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.051137 | +24.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUEL-EUR | 0.0008727 | +23.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FET-EUR | 0.20632 | +20.45 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.0382 | +19.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0082563 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1433 scans ; 613259 observations ; 825 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
