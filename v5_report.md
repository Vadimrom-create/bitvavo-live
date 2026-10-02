# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T05:01:52.100967+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-02T05:01:25.748682+00:00 | âge ticker : 142.6 s | durée : 143.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.6606 € | IGNITION | score 93.44/100 | entrée 6.85/10
  Entrée 1.664 € ; stop 1.5883 € ; TP1 1.8153 € ; TP2 1.891 € ; montant 229.30 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.22/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.22767 € | IGNITION | score 89.28/100 | entrée 7.60/10
  Entrée 0.22758 € ; stop 0.21958 € ; TP1 0.24358 € ; TP2 0.25158 € ; montant 250.00 € ; risque théorique 10.51 € ; R/R net 1.50.
  Chase risk : 4.639/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.093507 € ; score 91.90/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.46778 € ; score 89.85/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012307 € ; score 88.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AZTEC-EUR : 0.015918 € ; score 88.46/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7634 € ; score 88.29/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000575 | +122.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.130267 | +55.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.030941 | +40.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.44167 | +25.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04709 | +20.56 % | DETECTED_EARLY | NONE | NONE |
| MOVR-EUR | 2.3659 | +19.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.1715 | +16.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20888 | +15.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.163752 | +14.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 165.68 | +13.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1957 scans ; 837588 observations ; 1523 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
