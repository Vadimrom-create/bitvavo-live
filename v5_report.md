# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T18:24:51.038285+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-01T18:23:53.661674+00:00 | âge ticker : 184.3 s | durée : 186.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- SUI-EUR : 1.05343 € | IGNITION | score 93.42/100 | entrée 7.80/10
  Entrée 1.05328 € ; stop 1.01401 € ; TP1 1.13181 € ; TP2 1.17108 € ; montant 250.00 € ; risque théorique 11.04 € ; R/R net 1.52.
  Chase risk : 4.699/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SYRUP-EUR : 0.21123 € | IGNITION | score 87.92/100 | entrée 7.20/10
  Entrée 0.21124 € ; stop 0.20302 € ; TP1 0.22768 € ; TP2 0.2359 € ; montant 250.00 € ; risque théorique 11.44 € ; R/R net 1.54.
  Chase risk : 2.343/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.20757 € | IGNITION | score 87.61/100 | entrée 7.85/10
  Entrée 0.20757 € ; stop 0.19835 € ; TP1 0.22601 € ; TP2 0.23523 € ; montant 29.60 € ; risque théorique 1.52 € ; R/R net 1.59.
  Chase risk : 4.466/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.34311 € ; score 90.94/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.0020627 € ; score 90.83/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.29166 € ; score 87.42/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.6221 € ; score 86.73/100 ; SURVEILLE ; STABILITY_HOLD, PORTFOLIO_LIMIT
- AXS-EUR : 1.0312 € ; score 86.16/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00065427 | +152.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6667 | +74.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0775847 | +31.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04837 | +30.52 % | DETECTED_EARLY | NONE | NONE |
| ALICE-EUR | 0.18312 | +28.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43555 | +26.90 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.177504 | +22.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.030915 | +20.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009551 | +17.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024178 | +16.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1924 scans ; 823398 observations ; 1486 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
