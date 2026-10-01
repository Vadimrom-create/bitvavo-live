# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T04:24:51.037656+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-10-01T04:24:20.258870+00:00 | âge ticker : 146.7 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : BELOW_EXCHANGE_MINIMUM
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.113902 € | IGNITION | score 93.14/100 | entrée 7.50/10
  Entrée 0.11396 € ; stop 0.109316 € ; TP1 0.123248 € ; TP2 0.127892 € ; montant 250.00 € ; risque théorique 11.90 € ; R/R net 1.56.
  Chase risk : 4.184/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AAVE-EUR : 147.61 € | IGNITION | score 82.96/100 | entrée 6.60/10
  Entrée 148.28 € ; stop 141.38 € ; TP1 162.08 € ; TP2 168.98 € ; montant 224.84 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.537/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FET-EUR : 0.2061 € ; score 88.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.2215 € ; score 88.10/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SAND-EUR : 0.039324 € ; score 87.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PEPE-EUR : 3.8522e-06 € ; score 87.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZEN-EUR : 6.5641 € ; score 86.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0848 | +85.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34876 | +45.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009179 | +36.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.34292 | +23.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.41754 | +22.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028768 | +21.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0186111 | +18.51 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.0621642 | +16.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAFE-EUR | 0.110867 | +15.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RED-EUR | 0.16156 | +13.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1885 scans ; 806628 observations ; 1438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
