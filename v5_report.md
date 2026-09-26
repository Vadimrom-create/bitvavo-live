# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T22:23:51.860344+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T22:23:18.988112+00:00 | âge ticker : 145.3 s | durée : 146.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.82141 € | IGNITION | score 90.77/100 | entrée 7.40/10
  Entrée 1.82321 € ; stop 1.75889 € ; TP1 1.95184 € ; TP2 2.01617 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 2.87/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 8.5469 € | IGNITION | score 79.27/100 | entrée 7.40/10
  Entrée 8.5357 € ; stop 8.2339 € ; TP1 9.1393 € ; TP2 9.4411 € ; montant 250.00 € ; risque théorique 10.56 € ; R/R net 1.50.
  Chase risk : 2.483/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CC-EUR : 0.11945 € ; score 94.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.41733 € ; score 92.29/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.08344 € ; score 92.04/100 ; SURVEILLE ; LOW_LIQUIDITY
- BLUR-EUR : 0.018741 € ; score 91.65/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.105158 € ; score 90.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016687 | +109.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006921 | +56.02 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.131425 | +50.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018927 | +36.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 114.353 | +33.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063585 | +24.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043868 | +20.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.67394 | +17.83 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.005964 | +17.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.52439 | +16.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1567 scans ; 670477 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
