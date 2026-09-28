# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T12:52:58.846770+00:00
État : OK | marchés EUR : 427 | V4 : 399 | données valides : 427
Récupération : 2026-09-28T12:52:01.729558+00:00 | âge ticker : 181.1 s | durée : 182.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : PORTFOLIO_LIMIT
- ONDO-EUR : 0.4675 € | IGNITION | score 91.27/100 | entrée 7.55/10
  Entrée 0.46749 € ; stop 0.4505 € ; TP1 0.50147 € ; TP2 0.51846 € ; montant 250.00 € ; risque théorique 10.80 € ; R/R net 1.51.
  Chase risk : 3.564/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LINK-EUR : 12.8524 € | IGNITION | score 87.76/100 | entrée 6.85/10
  Entrée 12.8455 € ; stop 12.1173 € ; TP1 14.3018 € ; TP2 15.03 € ; montant 189.00 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 7.305/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- POL-EUR : 0.104032 € | IGNITION | score 84.60/100 | entrée 6.65/10
  Entrée 0.10385 € ; stop 0.099454 € ; TP1 0.112641 € ; TP2 0.117037 € ; montant 24.32 € ; risque théorique 1.20 € ; R/R net 1.57.
  Chase risk : 7.279/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WLD-EUR : 0.4544 € ; score 93.99/100 ; SURVEILLE ; WICK_SETUP
- W-EUR : 0.012722 € ; score 93.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72919 € ; score 90.83/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.2059 € ; score 90.60/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZK-EUR : 0.011114 € ; score 90.26/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 202.961 | +44.97 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.106271 | +26.53 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0046557 | +16.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.028575 | +16.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.489 | +12.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.11651 | +10.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.0018212 | +10.59 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ALGO-EUR | 0.114898 | +10.56 % | DETECTED_EARLY | NONE | NONE |
| AZTEC-EUR | 0.016409 | +10.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.02556 | +10.03 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1695 scans ; 725133 observations ; 1245 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
