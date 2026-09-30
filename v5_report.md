# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T17:42:42.074234+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-09-30T17:42:04.964787+00:00 | âge ticker : 166.2 s | durée : 167.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZIG-EUR : 0.04823 € | IGNITION | score 81.98/100 | entrée 6.95/10
  Entrée 0.048412 € ; stop 0.045949 € ; TP1 0.053337 € ; TP2 0.0558 € ; montant 207.98 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.003/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COMP-EUR : 21.859 € ; score 84.40/100 ; SURVEILLE ; seuil achat non atteint
- DRV-EUR : 0.3402 € ; score 84.28/100 ; SURVEILLE ; SPREAD_RISK
- SOLV-EUR : 0.0038275 € ; score 84.08/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- LUNA2-EUR : 0.045254 € ; score 83.91/100 ; SURVEILLE ; LOW_LIQUIDITY
- ALGO-EUR : 0.109904 € ; score 83.44/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.4353 | +51.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.33313 | +39.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| UP-EUR | 0.08073 | +32.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.43642 | +23.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 267.131 | +21.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007899 | +20.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.002142 | +19.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.32015 | +15.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MERL-EUR | 0.028316 | +14.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.068 | +12.53 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1853 scans ; 792868 observations ; 1415 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
