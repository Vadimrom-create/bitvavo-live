# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T07:21:56.508480+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T07:21:25.285176+00:00 | âge ticker : 146.0 s | durée : 147.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XDC-EUR : 0.026734 € ; score 89.49/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0019148 € ; score 88.91/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- DOT-EUR : 1.0848 € ; score 88.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.29208 € ; score 88.84/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0019081 € ; score 87.74/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0015491 | +98.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019785 | +72.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24381 | +38.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.06891 | +38.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.062444 | +31.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AERO-EUR | 0.79552 | +25.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23617 | +21.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.12177 | +18.30 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KMNO-EUR | 0.038284 | +17.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0040058 | +17.37 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1512 scans ; 646992 observations ; 956 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
