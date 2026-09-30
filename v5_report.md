# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T22:56:36.650700+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T22:56:06.995515+00:00 | âge ticker : 145.3 s | durée : 146.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0169482 € | IGNITION | score 92.68/100 | entrée 7.45/10
  Entrée 0.0169486 € ; stop 0.0162735 € ; TP1 0.0182988 € ; TP2 0.0189739 € ; montant 250.00 € ; risque théorique 11.67 € ; R/R net 1.55.
  Chase risk : 4.938/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CRV-EUR : 0.34822 € ; score 93.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.3632e-06 € ; score 90.97/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.71551 € ; score 90.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MEW-EUR : 0.00044092 € ; score 89.63/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.110508 € ; score 88.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.8717 | +75.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35383 | +48.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.4387 | +22.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008177 | +19.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33401 | +18.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0603537 | +14.39 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOMI-EUR | 0.19879 | +11.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.026677 | +10.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| WLD-EUR | 0.47657 | +10.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015043 | +10.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1869 scans ; 799748 observations ; 1425 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
