# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T20:27:14.221326+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T20:26:40.811356+00:00 | âge ticker : 154.5 s | durée : 155.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.070877 € ; score 91.29/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.20825 € ; score 90.46/100 ; SURVEILLE ; SPREAD_RISK
- SEI-EUR : 0.065389 € ; score 88.82/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.21194 € ; score 86.72/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72129 € ; score 85.00/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017709 | +40.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.68972 | +36.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.29068 | +23.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.359 | +22.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021077 | +19.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 1.0142 | +18.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICP-EUR | 3.1094 | +16.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0052106 | +14.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.061321 | +13.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 146.48 | +12.50 % | DETECTED_EARLY | NONE | NONE |

Historique : 1791 scans ; 766249 observations ; 1338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
