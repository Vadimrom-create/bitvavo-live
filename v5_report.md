# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T10:12:55.877752+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-21T10:12:24.807813+00:00 | âge ticker : 154.3 s | durée : 155.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- PORTAL-EUR : 0.017799 € | IGNITION | score 86.29/100 | entrée 6.80/10
  Entrée 0.017786 € ; stop 0.016964 € ; TP1 0.01943 € ; TP2 0.020252 € ; montant 226.18 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 6.488/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- STX-EUR : 0.28882 € | IGNITION | score 79.07/100 | entrée 6.90/10
  Entrée 0.28873 € ; stop 0.277 € ; TP1 0.31218 € ; TP2 0.32391 € ; montant 250.00 € ; risque théorique 11.87 € ; R/R net 1.56.
  Chase risk : 3.183/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DOT-EUR : 1.0247 € ; score 91.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MANTA-EUR : 0.061181 € ; score 90.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RUNE-EUR : 0.51545 € ; score 89.03/100 ; SURVEILLE ; seuil achat non atteint
- ARX-EUR : 0.17393 € ; score 88.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 51.787 € ; score 87.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055962 | +70.28 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.051714 | +65.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009592 | +54.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057872 | +34.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030516 | +33.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23763 | +29.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.016221 | +29.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030907 | +26.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031872 | +25.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.088502 | +23.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1067 scans ; 457279 observations ; 338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
