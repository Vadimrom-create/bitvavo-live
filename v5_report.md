# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T09:49:02.680201+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-26T09:48:31.127443+00:00 | âge ticker : 147.7 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.104038 € | IGNITION | score 80.66/100 | entrée 7.15/10
  Entrée 0.104207 € ; stop 0.099113 € ; TP1 0.114394 € ; TP2 0.119488 € ; montant 215.39 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 4.006/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AXS-EUR : 1.0542 € ; score 94.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- IOST-EUR : 0.0008423 € ; score 92.00/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- C-EUR : 0.078419 € ; score 91.86/100 ; SURVEILLE ; seuil achat non atteint
- ARKM-EUR : 0.12153 € ; score 91.58/100 ; SURVEILLE ; LOW_LIQUIDITY
- ID-EUR : 0.034658 € ; score 90.43/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020439 | +163.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019316 | +66.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.068164 | +40.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.2421 | +32.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.067178 | +29.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.24318 | +22.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.79309 | +17.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.097734 | +16.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.5364 | +15.93 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TNSR-EUR | 0.038898 | +15.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1521 scans ; 650835 observations ; 968 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
