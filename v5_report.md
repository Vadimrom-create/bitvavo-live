# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T22:38:00.597712+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T22:37:00.338429+00:00 | âge ticker : 180.9 s | durée : 181.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WAL-EUR : 0.029962 € ; score 92.20/100 ; SURVEILLE ; seuil achat non atteint
- MOODENG-EUR : 0.043026 € ; score 91.82/100 ; SURVEILLE ; WICK_SETUP
- BABY-EUR : 0.011204 € ; score 88.73/100 ; SURVEILLE ; WICK_SETUP
- DATAIP-EUR : 0.2006 € ; score 86.32/100 ; SURVEILLE ; WICK_SETUP
- POL-EUR : 0.095452 € ; score 85.94/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.059252 | +39.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0089125 | +29.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.59977 | +27.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 79.399 | +27.45 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.4569 | +25.93 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.039268 | +25.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.38113 | +25.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.17055 | +23.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.09494 | +18.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.020982 | +17.60 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1396 scans ; 597460 observations ; 766 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
