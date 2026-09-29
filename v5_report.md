# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T04:37:26.416411+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T04:36:53.915697+00:00 | âge ticker : 156.2 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- W-EUR : 0.012306 € ; score 91.73/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.67514 € ; score 90.68/100 ; SURVEILLE ; seuil achat non atteint
- PHA-EUR : 0.05551 € ; score 87.66/100 ; SURVEILLE ; WICK_SETUP
- GLMR-EUR : 0.006776 € ; score 87.07/100 ; SURVEILLE ; seuil achat non atteint
- ETHFI-EUR : 0.60336 € ; score 86.16/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.1354 | +38.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105396 | +25.46 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.120569 | +17.14 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26064 | +16.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.33931 | +15.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.090861 | +10.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.59732 | +9.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22802 | +7.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048429 | +7.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0017901 | +7.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1745 scans ; 746533 observations ; 1281 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
