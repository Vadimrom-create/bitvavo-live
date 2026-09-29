# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T06:38:28.090933+00:00
État : OK | marchés EUR : 428 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T06:37:57.943281+00:00 | âge ticker : 151.1 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.6023 € | IGNITION | score 88.13/100 | entrée 7.60/10
  Entrée 9.5927 € ; stop 9.0861 € ; TP1 10.6059 € ; TP2 11.1125 € ; montant 201.25 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 3.771/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AERO-EUR : 0.75006 € | IGNITION | score 87.67/100 | entrée 6.55/10
  Entrée 0.75221 € ; stop 0.72331 € ; TP1 0.81001 € ; TP2 0.83891 € ; montant 250.00 € ; risque théorique 11.32 € ; R/R net 1.54.
  Chase risk : 5.712/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AAVE-EUR : 137.41 € | IGNITION | score 77.48/100 | entrée 6.60/10
  Entrée 137.43 € ; stop 129.73 € ; TP1 152.83 € ; TP2 160.53 € ; montant 10.80 € ; risque théorique 0.68 € ; R/R net 1.67.
  Chase risk : 5.814/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FET-EUR : 0.19807 € ; score 91.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WOO-EUR : 0.011739 € ; score 89.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.2012 € ; score 89.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.040474 € ; score 89.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.012623 € ; score 89.14/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.3757 | +29.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.103307 | +20.75 % | DETECTED_EARLY | NONE | NONE |
| CRV-EUR | 0.34955 | +19.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.27018 | +18.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.24112 | +14.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.091326 | +14.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.116656 | +13.63 % | DETECTED_EARLY | NONE | NONE |
| CVX-EUR | 2.0188 | +11.08 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PHA-EUR | 0.058212 | +10.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.14628 | +10.28 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1751 scans ; 749101 observations ; 1284 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
