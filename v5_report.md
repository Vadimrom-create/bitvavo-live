# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T06:27:00.042417+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T06:26:24.347055+00:00 | âge ticker : 157.4 s | durée : 159.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.8137 € ; score 87.00/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.93125 € ; score 86.54/100 ; SURVEILLE ; seuil achat non atteint
- RLC-EUR : 0.32014 € ; score 83.92/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- LTC-EUR : 63.518 € ; score 82.54/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.0057146 € ; score 82.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0015155 | +92.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.073658 | +50.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24545 | +48.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.016048 | +39.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.79189 | +25.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.059629 | +24.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENA-EUR | 0.23425 | +20.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.101083 | +18.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.004028 | +17.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037843 | +16.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1509 scans ; 645711 observations ; 955 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
