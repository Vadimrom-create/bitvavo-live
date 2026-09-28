# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T12:26:52.547421+00:00
État : OK | marchés EUR : 427 | V4 : 399 | données valides : 427
Récupération : 2026-09-28T12:26:21.286567+00:00 | âge ticker : 146.2 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ADA-EUR : 0.22211 € | IGNITION | score 89.02/100 | entrée 7.35/10
  Entrée 0.22202 € ; stop 0.21339 € ; TP1 0.23928 € ; TP2 0.24791 € ; montant 250.00 € ; risque théorique 11.43 € ; R/R net 1.54.
  Chase risk : 3.216/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- POL-EUR : 0.104177 € | IGNITION | score 83.41/100 | entrée 6.90/10
  Entrée 0.103892 € ; stop 0.09914 € ; TP1 0.113395 € ; TP2 0.118147 € ; montant 228.22 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.371/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- EIGEN-EUR : 0.23007 € ; score 89.04/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.305 € ; score 88.85/100 ; SURVEILLE ; WICK_SETUP
- WOO-EUR : 0.011802 € ; score 88.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BONK-EUR : 3.1034e-06 € ; score 88.44/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.011105 € ; score 88.42/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 208.695 | +44.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.10879 | +30.08 % | DETECTED_EARLY | NONE | NONE |
| GRT-EUR | 0.028991 | +16.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.7223 | +14.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0044757 | +13.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.116575 | +12.46 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.025862 | +10.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048471 | +9.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.00181 | +8.98 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SEI-EUR | 0.071324 | +8.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1694 scans ; 724706 observations ; 1245 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
