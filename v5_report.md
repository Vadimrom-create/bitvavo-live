# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T08:44:35.947136+00:00
État : OK | marchés EUR : 426 | V4 : 378 | données valides : 426
Récupération : 2026-09-21T08:44:12.425871+00:00 | âge ticker : 148.1 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LDO-EUR : SPREAD_RISK, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 101 € | IGNITION | score 91.35/100 | entrée 7.85/10
  Entrée 101.058 € ; stop 96.802 € ; TP1 109.57 € ; TP2 113.826 € ; montant 245.06 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.175/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- STX-EUR : 0.28476 € | IGNITION | score 89.05/100 | entrée 7.25/10
  Entrée 0.28573 € ; stop 0.27547 € ; TP1 0.30624 € ; TP2 0.3165 € ; montant 250.00 € ; risque théorique 10.70 € ; R/R net 1.51.
  Chase risk : 1.91/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COW-EUR : 0.13545 € ; score 93.26/100 ; SURVEILLE ; WICK_SETUP
- LDO-EUR : 0.3797 € ; score 92.50/100 ; SURVEILLE ; SPREAD_RISK, INSUFFICIENT_NET_RISK_REWARD
- ACH-EUR : 0.0052043 € ; score 92.11/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZK-EUR : 0.010547 € ; score 92.06/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- VET-EUR : 0.0075167 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056527 | +70.23 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009714 | +59.82 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.033687 | +38.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.058802 | +36.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24422 | +33.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.030473 | +29.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.51874 | +27.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.038354 | +23.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 29.9317 | +23.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031 | +22.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1061 scans ; 454723 observations ; 332 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
