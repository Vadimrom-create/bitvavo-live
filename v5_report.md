# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T13:10:02.679547+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 427
Récupération : 2026-09-28T13:09:32.029369+00:00 | âge ticker : 154.1 s | durée : 157.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : BELOW_EXCHANGE_MINIMUM
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- LINK-EUR : 12.7959 € | IGNITION | score 92.93/100 | entrée 7.70/10
  Entrée 12.7916 € ; stop 12.153 € ; TP1 14.0688 € ; TP2 14.7074 € ; montant 211.46 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 8.576/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.19735 € | IGNITION | score 81.87/100 | entrée 6.85/10
  Entrée 0.19727 € ; stop 0.18481 € ; TP1 0.22219 € ; TP2 0.23465 € ; montant 171.57 € ; risque théorique 12.00 € ; R/R net 1.70.
  Chase risk : 8.972/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.012733 € ; score 93.52/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SNX-EUR : 0.21863 € ; score 89.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.723 € ; score 89.11/100 ; SURVEILLE ; WICK_SETUP
- GMT-EUR : 0.007515 € ; score 88.28/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.30442 € ; score 87.24/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XDP-EUR | 0.042836 | +69.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| QNT-EUR | 204.015 | +44.13 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.102973 | +25.32 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0046838 | +18.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.028256 | +15.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.27858 | +13.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NMR-EUR | 9.62 | +13.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.114429 | +11.81 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.025622 | +11.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.016144 | +9.59 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1696 scans ; 725561 observations ; 1245 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
