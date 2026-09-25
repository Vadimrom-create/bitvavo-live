# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T06:34:28.662233+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T06:33:56.963364+00:00 | âge ticker : 146.8 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- THE-EUR : 0.0756 € ; score 87.95/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.20194 € ; score 87.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.007666 € ; score 87.02/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.07927 € ; score 84.68/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.10262 € ; score 83.02/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 85.821 | +36.42 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.104749 | +31.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.65 | +31.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.4749 | +24.64 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038792 | +21.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086736 | +19.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.048999 | +19.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.022057 | +18.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0081902 | +15.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRC-EUR | 0.0011509 | +14.79 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1423 scans ; 608989 observations ; 816 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
