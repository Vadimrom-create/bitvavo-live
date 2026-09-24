# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:01:12.294593+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T20:00:38.813995+00:00 | âge ticker : 158.2 s | durée : 160.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VVV-EUR : 27.9657 € | IGNITION | score 82.87/100 | entrée 7.20/10
  Entrée 27.9311 € ; stop 26.3649 € ; TP1 31.0635 € ; TP2 32.6297 € ; montant 190.85 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 5.601/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.19716 € | IGNITION | score 81.17/100 | entrée 7.35/10
  Entrée 0.19724 € ; stop 0.18977 € ; TP1 0.21218 € ; TP2 0.21965 € ; montant 250.00 € ; risque théorique 11.19 € ; R/R net 1.53.
  Chase risk : 4.814/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZIG-EUR : 0.045421 € ; score 91.81/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 261.78 € ; score 91.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : 0.1942 € ; score 91.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CVC-EUR : 0.026448 € ; score 89.82/100 ; SURVEILLE ; seuil achat non atteint
- THE-EUR : 0.07489 € ; score 88.17/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.67684 | +44.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0095736 | +39.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38136 | +34.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44843 | +24.05 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0019666 | +23.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 75.654 | +21.43 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.094195 | +20.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.037074 | +19.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0161809 | +19.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16358 | +17.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1383 scans ; 591909 observations ; 758 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
