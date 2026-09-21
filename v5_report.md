# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T14:22:12.407492+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-21T14:21:39.756446+00:00 | âge ticker : 154.0 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MIRA-EUR : 0.046953 € ; score 89.81/100 ; SURVEILLE ; seuil achat non atteint
- ENS-EUR : 5.8152 € ; score 89.05/100 ; SURVEILLE ; seuil achat non atteint
- CTSI-EUR : 0.025506 € ; score 86.56/100 ; SURVEILLE ; SPREAD_RISK
- GRASS-EUR : 0.32703 € ; score 85.52/100 ; SURVEILLE ; seuil achat non atteint
- COW-EUR : 0.13582 € ; score 85.47/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055377 | +68.40 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.048499 | +52.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009651 | +43.57 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.103069 | +38.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.24288 | +32.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.031182 | +29.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.056469 | +29.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.90529 | +26.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.052242 | +26.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AKT-EUR | 0.58749 | +24.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1082 scans ; 463669 observations ; 380 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
