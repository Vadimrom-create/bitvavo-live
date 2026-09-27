# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T17:56:37.815110+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T17:56:05.610293+00:00 | âge ticker : 157.1 s | durée : 158.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GALA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ENA-EUR : 0.24722 € | IGNITION | score 82.21/100 | entrée 6.80/10
  Entrée 0.24647 € ; stop 0.23708 € ; TP1 0.26525 € ; TP2 0.27463 € ; montant 250.00 € ; risque théorique 11.24 € ; R/R net 1.53.
  Chase risk : 2.14/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZK-EUR : 0.011535 € ; score 93.77/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- MOVR-EUR : 0.9365 € ; score 92.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- APE-EUR : 0.14639 € ; score 91.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XAI-EUR : 0.0085138 € ; score 90.93/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.0421 € ; score 89.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 162.7 | +51.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28265 | +46.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.07013 | +46.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.015952 | +25.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006467 | +24.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.2464 | +20.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013642 | +19.99 % | DETECTED_EARLY | NONE | NONE |
| GLMR-EUR | 0.007122 | +17.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.56313 | +17.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006998 | +15.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1635 scans ; 699513 observations ; 1163 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
