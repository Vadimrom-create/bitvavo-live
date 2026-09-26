# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T11:53:15.580739+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T11:52:45.521367+00:00 | âge ticker : 143.4 s | durée : 144.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.6087 € | IGNITION | score 89.30/100 | entrée 7.85/10
  Entrée 9.609 € ; stop 9.2227 € ; TP1 10.3816 € ; TP2 10.7679 € ; montant 250.00 € ; risque théorique 11.77 € ; R/R net 1.55.
  Chase risk : 3.235/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAO-EUR : 288.88 € | IGNITION | score 83.42/100 | entrée 7.60/10
  Entrée 289.11 € ; stop 272.88 € ; TP1 321.57 € ; TP2 337.8 € ; montant 190.65 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 3.654/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FORM-EUR : 0.28903 € ; score 92.77/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.08354 € ; score 91.89/100 ; SURVEILLE ; LOW_LIQUIDITY
- JUP-EUR : 0.30852 € ; score 88.75/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TWT-EUR : 0.527 € ; score 88.40/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- STRK-EUR : 0.037301 € ; score 88.24/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0022605 | +182.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020915 | +76.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.072256 | +32.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.063497 | +30.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AMP-EUR | 0.0005639 | +27.03 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.7689 | +20.56 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.24482 | +20.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENA-EUR | 0.2478 | +17.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.80836 | +17.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.041028 | +14.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1529 scans ; 654251 observations ; 982 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
