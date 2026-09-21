# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T14:00:15.423284+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-21T13:59:45.288098+00:00 | âge ticker : 152.8 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GRASS-EUR : 0.32632 € ; score 93.06/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 102.9 € ; score 88.49/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.007143 € ; score 87.71/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- MIRA-EUR : 0.046953 € ; score 87.06/100 ; SURVEILLE ; SPREAD_RISK
- INJ-EUR : 6.9667 € ; score 86.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.054454 | +64.93 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.050767 | +61.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009716 | +45.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.104234 | +39.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.031358 | +30.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24038 | +29.94 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SEI-EUR | 0.053102 | +28.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROVE-EUR | 0.2487 | +28.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.055738 | +27.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.90263 | +26.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1081 scans ; 463243 observations ; 378 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
