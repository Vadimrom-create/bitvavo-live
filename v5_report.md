# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T08:45:49.645181+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T08:45:23.759994+00:00 | âge ticker : 148.3 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.0626 € | IGNITION | score 81.97/100 | entrée 6.90/10
  Entrée 4.0638 € ; stop 3.8968 € ; TP1 4.3977 € ; TP2 4.5647 € ; montant 250.00 € ; risque théorique 11.99 € ; R/R net 1.56.
  Chase risk : 3.636/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.6517 € ; score 92.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DRIFT-EUR : 0.01662 € ; score 89.96/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SUI-EUR : 0.90177 € ; score 89.70/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MORPHO-EUR : 2.55493 € ; score 89.41/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0081709 € ; score 88.56/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.79197 | +59.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.109692 | +39.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 86.029 | +38.48 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.49622 | +31.48 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.19506 | +28.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.049894 | +21.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUEL-EUR | 0.0008489 | +20.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.021409 | +19.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.008333 | +19.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LDO-EUR | 0.41049 | +18.79 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1431 scans ; 612405 observations ; 820 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
