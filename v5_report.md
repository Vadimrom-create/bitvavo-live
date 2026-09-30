# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T09:22:47.560159+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T09:22:14.223459+00:00 | âge ticker : 154.2 s | durée : 155.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.35561 € | IGNITION | score 89.67/100 | entrée 7.20/10
  Entrée 0.35593 € ; stop 0.34206 € ; TP1 0.38367 € ; TP2 0.39754 € ; montant 250.00 € ; risque théorique 11.46 € ; R/R net 1.54.
  Chase risk : 3.976/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.0897 € | IGNITION | score 88.40/100 | entrée 7.30/10
  Entrée 1.0901 € ; stop 1.0476 € ; TP1 1.1751 € ; TP2 1.2176 € ; montant 250.00 € ; risque théorique 11.46 € ; R/R net 1.54.
  Chase risk : 3.814/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WLD-EUR : 0.4552 € ; score 87.38/100 ; SURVEILLE ; WICK_SETUP
- LPT-EUR : 1.551 € ; score 86.19/100 ; SURVEILLE ; WICK_SETUP
- SAND-EUR : 0.039929 € ; score 85.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- COMP-EUR : 22.487 € ; score 85.58/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.94789 € ; score 85.26/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.7376 | +98.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.102532 | +34.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008997 | +31.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.39318 | +28.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.0727 | +25.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.25935 | +19.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0022581 | +15.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0050905 | +14.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29944 | +14.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.5574 | +13.94 % | DETECTED_EARLY | NONE | NONE |

Historique : 1830 scans ; 782980 observations ; 1365 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
