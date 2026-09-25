# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T09:00:27.464899+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-25T08:59:59.837401+00:00 | âge ticker : 149.9 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.27772 € ; score 94.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.90232 € ; score 92.04/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.024972 € ; score 91.60/100 ; SURVEILLE ; seuil achat non atteint
- MET-EUR : 0.29401 € ; score 90.65/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.2213 € ; score 90.54/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.77158 | +54.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 87.254 | +39.99 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.104909 | +33.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.49534 | +31.39 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.19567 | +28.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FUEL-EUR | 0.0009011 | +27.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.050559 | +22.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021343 | +19.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.2048 | +18.40 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038003 | +17.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1432 scans ; 612832 observations ; 822 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
