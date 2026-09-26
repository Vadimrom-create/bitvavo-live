# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T02:46:12.365048+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T02:45:42.455912+00:00 | âge ticker : 149.8 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.103163 € ; score 93.86/100 ; SURVEILLE ; WICK_SETUP
- POL-EUR : 0.103771 € ; score 90.05/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COMP-EUR : 21.265 € ; score 88.12/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.57836 € ; score 85.48/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- LINK-EUR : 12.319 € ; score 84.24/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.074443 | +70.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0012076 | +55.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.23296 | +39.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.77242 | +27.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.104489 | +18.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.021653 | +18.12 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RARE-EUR | 0.013309 | +17.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.065413 | +17.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23334 | +17.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.73446 | +16.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1496 scans ; 640160 observations ; 931 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
