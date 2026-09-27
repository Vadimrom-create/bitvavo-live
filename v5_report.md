# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T21:21:45.185488+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-27T21:20:49.053418+00:00 | âge ticker : 172.1 s | durée : 173.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.2062 € ; score 93.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOODENG-EUR : 0.043044 € ; score 88.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- OP-EUR : 0.12919 € ; score 87.74/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.71956 € ; score 87.71/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BAT-EUR : 0.08482 € ; score 87.49/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 176.556 | +63.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.2852 | +41.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.00667 | +30.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.92345 | +23.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.028949 | +19.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.01358 | +19.27 % | DETECTED_EARLY | NONE | NONE |
| AUDIO-EUR | 0.015372 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.004426 | +15.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0011606 | +14.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 4.865 | +14.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1647 scans ; 704637 observations ; 1174 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
