# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T17:57:43.240820+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-01T17:57:17.035306+00:00 | âge ticker : 147.5 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : BELOW_EXCHANGE_MINIMUM
- SUI-EUR : 1.05509 € | IGNITION | score 92.14/100 | entrée 7.60/10
  Entrée 1.05519 € ; stop 1.00429 € ; TP1 1.15699 € ; TP2 1.20789 € ; montant 217.91 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.482/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AAVE-EUR : 152.1 € | IGNITION | score 91.04/100 | entrée 7.45/10
  Entrée 152.15 € ; stop 145.48 € ; TP1 165.49 € ; TP2 172.16 € ; montant 236.76 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.451/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0020547 € ; score 92.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.007595 € ; score 90.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- JUP-EUR : 0.29004 € ; score 89.52/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.5476 € ; score 89.01/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- AVAX-EUR : 9.7487 € ; score 88.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00065046 | +151.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.612 | +71.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.077866 | +33.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.43338 | +28.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.183 | +28.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04732 | +27.03 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.179616 | +22.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.49384 | +20.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.030754 | +20.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.096826 | +15.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1923 scans ; 822968 observations ; 1486 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
