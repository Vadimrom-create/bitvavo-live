# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T06:30:05.564047+00:00
État : OK | marchés EUR : 426 | V4 : 374 | données valides : 426
Récupération : 2026-09-21T06:29:35.387741+00:00 | âge ticker : 147.6 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.38161 € | IGNITION | score 92.93/100 | entrée 8.05/10
  Entrée 0.38123 € ; stop 0.36773 € ; TP1 0.40823 € ; TP2 0.42173 € ; montant 250.00 € ; risque théorique 10.57 € ; R/R net 1.50.
  Chase risk : 3.133/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- APT-EUR : 0.6685 € | IGNITION | score 87.55/100 | entrée 6.95/10
  Entrée 0.6671 € ; stop 0.6379 € ; TP1 0.7255 € ; TP2 0.7547 € ; montant 237.07 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.297/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.035009 € ; score 91.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 234.87 € ; score 86.56/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.20435 € ; score 85.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.17394 € ; score 85.00/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.5244e-06 € ; score 84.96/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056034 | +68.11 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009681 | +57.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.064895 | +49.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.25081 | +37.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030495 | +26.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029404 | +24.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7182 | +23.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.050599 | +21.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.50111 | +21.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 28.593 | +21.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1053 scans ; 451315 observations ; 328 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
