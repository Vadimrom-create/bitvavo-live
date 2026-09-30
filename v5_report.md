# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T11:42:07.255875+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T11:41:36.800544+00:00 | âge ticker : 146.9 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.6591 € | IGNITION | score 79.81/100 | entrée 7.40/10
  Entrée 4.6598 € ; stop 4.4357 € ; TP1 5.108 € ; TP2 5.3321 € ; montant 218.48 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 6.25/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.095309 € ; score 91.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.14674 € ; score 91.92/100 ; SURVEILLE ; LOW_LIQUIDITY
- ICP-EUR : 3.0233 € ; score 90.61/100 ; SURVEILLE ; seuil achat non atteint
- CAT-EUR : 2.025e-06 € ; score 89.48/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- LINEA-EUR : 0.002574 € ; score 88.89/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.611 | +78.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.39463 | +65.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ARK-EUR | 0.33499 | +55.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.38833 | +32.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 281.413 | +27.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008148 | +22.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.094431 | +22.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.065576 | +15.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.084049 | +13.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.4039 | +11.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1837 scans ; 785988 observations ; 1370 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
