# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T20:49:43.372179+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-26T20:49:11.028913+00:00 | âge ticker : 149.0 s | durée : 149.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- EIGEN-EUR : 0.233 € ; score 94.19/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.704 € ; score 93.40/100 ; SURVEILLE ; seuil achat non atteint
- BLUR-EUR : 0.018181 € ; score 92.12/100 ; SURVEILLE ; SPREAD_RISK
- MANA-EUR : 0.079241 € ; score 90.89/100 ; SURVEILLE ; seuil achat non atteint
- VTHO-EUR : 0.0006982 € ; score 88.46/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016908 | +108.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0007099 | +60.03 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.128232 | +46.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019374 | +39.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 105.742 | +23.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006248 | +22.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.043605 | +18.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.060777 | +17.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.736 | +16.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LAPTOP-EUR | 0.07467 | +15.73 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1561 scans ; 667915 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
