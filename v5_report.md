# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T12:13:43.542532+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-09-21T12:13:12.862207+00:00 | âge ticker : 148.4 s | durée : 149.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.007868 € | IGNITION | score 92.01/100 | entrée 7.60/10
  Entrée 0.0078718 € ; stop 0.0074982 € ; TP1 0.008619 € ; TP2 0.0089926 € ; montant 221.02 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.05/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PEPE-EUR : 3.6777e-06 € | IGNITION | score 81.94/100 | entrée 7.45/10
  Entrée 3.6893e-06 € ; stop 3.5577e-06 € ; TP1 3.9525e-06 € ; TP2 4.0841e-06 € ; montant 250.00 € ; risque théorique 10.64 € ; R/R net 1.51.
  Chase risk : 2.766/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAIKO-EUR : 0.07974 € ; score 92.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.055753 € ; score 89.85/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AZTEC-EUR : 0.014434 € ; score 88.08/100 ; SURVEILLE ; SPREAD_RISK
- BNB-EUR : 688.16 € ; score 87.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.029914 € ; score 86.33/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.058 | +73.30 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.052793 | +66.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009885 | +39.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.031472 | +32.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.056159 | +30.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.096836 | +27.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.052921 | +27.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.22999 | +25.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.031892 | +25.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.88713 | +23.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1075 scans ; 460687 observations ; 354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
