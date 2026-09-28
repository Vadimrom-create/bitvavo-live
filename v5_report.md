# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T02:23:29.774632+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-28T02:22:58.529039+00:00 | âge ticker : 148.2 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.50711 € | IGNITION | score 80.09/100 | entrée 7.60/10
  Entrée 0.50635 € ; stop 0.48363 € ; TP1 0.55178 € ; TP2 0.5745 € ; montant 232.05 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.191/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LDO-EUR : 0.42781 € ; score 92.48/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.11542 € ; score 92.40/100 ; SURVEILLE ; WICK_SETUP
- GRAM-EUR : 1.4504 € ; score 85.56/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICNT-EUR : 0.08723 € ; score 82.81/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- POL-EUR : 0.104309 € ; score 82.69/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 229.613 | +49.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.0971 | +31.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030448 | +27.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26986 | +25.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IRYS-EUR | 0.017997 | +23.12 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| INX-EUR | 0.006227 | +19.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0045417 | +17.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.58629 | +17.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.07507 | +17.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16611 | +13.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1665 scans ; 712323 observations ; 1216 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
