# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T15:26:34.213200+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 428
Récupération : 2026-09-29T15:26:00.773987+00:00 | âge ticker : 147.7 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.4463 € ; score 87.36/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0037922 € ; score 83.89/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.045891 € ; score 83.16/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.113764 € ; score 81.65/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0020174 € ; score 81.18/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.2983 | +37.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016886 | +34.70 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0021926 | +24.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.35628 | +23.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.61053 | +22.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.096087 | +20.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 150.94 | +17.87 % | DETECTED_EARLY | NONE | NONE |
| CELO-EUR | 0.094201 | +17.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21265 | +15.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 2.9536 | +14.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1776 scans ; 759814 observations ; 1319 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
