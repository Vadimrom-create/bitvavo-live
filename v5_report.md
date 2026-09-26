# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T08:27:14.389490+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T08:26:44.837274+00:00 | âge ticker : 148.1 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 64.476 € ; score 93.85/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LPT-EUR : 1.5542 € ; score 91.12/100 ; SURVEILLE ; seuil achat non atteint
- ALICE-EUR : 0.14451 € ; score 90.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- THQ-EUR : 0.011676 € ; score 90.04/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- LDO-EUR : 0.4315 € ; score 89.73/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017508 | +122.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018717 | +62.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.067342 | +37.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.06482 | +33.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24748 | +33.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24127 | +23.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.77797 | +18.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038282 | +16.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0039453 | +16.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.12002 | +15.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1516 scans ; 648700 observations ; 963 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
