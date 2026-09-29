# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T06:59:21.366795+00:00
État : OK | marchés EUR : 428 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T06:58:53.613250+00:00 | âge ticker : 148.4 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- FET-EUR : BELOW_EXCHANGE_MINIMUM
- GALA-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- ICP-EUR : BELOW_EXCHANGE_MINIMUM
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEAQ-EUR : BELOW_EXCHANGE_MINIMUM
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : BELOW_EXCHANGE_MINIMUM
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- XDC-EUR : 0.030923 € | IGNITION | score 92.43/100 | entrée 7.65/10
  Entrée 0.030887 € ; stop 0.029599 € ; TP1 0.033463 € ; TP2 0.034751 € ; montant 247.15 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.842/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.46032 € | IGNITION | score 91.92/100 | entrée 8.05/10
  Entrée 0.45998 € ; stop 0.44057 € ; TP1 0.49879 € ; TP2 0.51821 € ; montant 244.65 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.87/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AZTEC-EUR : 0.016765 € ; score 92.94/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.20093 € ; score 91.46/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- LTC-EUR : 60.391 € ; score 91.46/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEAQ-EUR : 0.03735 € ; score 90.43/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- VIRTUAL-EUR : 0.721 € ; score 90.36/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.2927 | +27.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.103799 | +21.79 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.2714 | +21.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35059 | +20.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.24466 | +16.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.091858 | +14.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.14846 | +13.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.116824 | +13.43 % | DETECTED_EARLY | NONE | NONE |
| CVX-EUR | 2.0188 | +11.22 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NPC-EUR | 0.0207337 | +10.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1752 scans ; 749529 observations ; 1284 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
