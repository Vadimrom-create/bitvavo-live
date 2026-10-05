# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T15:11:20.848486+00:00
État : OK | marchés EUR : 427 | V4 : 367 | données valides : 426
Récupération : 2026-10-05T15:10:17.353476+00:00 | âge ticker : 181.9 s | durée : 183.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SENT-EUR : 0.021611 € ; score 91.63/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.12033 € ; score 88.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- YGG-EUR : 0.02574 € ; score 85.40/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- PTB-EUR : 0.0009014 € ; score 84.45/100 ; SURVEILLE ; WICK_SETUP
- ICP-EUR : 3.0779 € ; score 81.34/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.190179 | +79.50 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.517 | +59.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.0715 | +45.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8494 | +19.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.8675 | +17.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046827 | +17.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SCR-EUR | 0.026022 | +16.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OGN-EUR | 0.02082 | +14.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.089358 | +14.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05193 | +11.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
