# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T22:35:47.394738+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T22:35:13.697777+00:00 | âge ticker : 154.7 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RSR-EUR : 0.0014653 € ; score 85.79/100 ; SURVEILLE ; seuil achat non atteint
- FLOKI-EUR : 2.4226e-05 € ; score 84.94/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.20756 € ; score 84.46/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LQTY-EUR : 0.20665 € ; score 84.10/100 ; SURVEILLE ; SPREAD_RISK
- DATAIP-EUR : 0.1975 € ; score 84.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001707 | +33.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66034 | +28.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0595 | +25.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002176 | +22.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051441 | +21.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29116 | +20.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.062796 | +19.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.35805 | +17.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDP-EUR | 0.021513 | +16.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUEL-EUR | 0.0006678 | +15.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1798 scans ; 769252 observations ; 1340 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
