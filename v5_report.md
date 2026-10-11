# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-11T20:39:42.329992+00:00
État : OK | marchés EUR : 427 | V4 : 374 | données valides : 427
Récupération : 2026-10-11T20:38:32.038115+00:00 | âge ticker : 186.9 s | durée : 188.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RAY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZK-EUR : 0.014261 € ; score 81.31/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- TIA-EUR : 0.51604 € ; score 77.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- FIL-EUR : 1.08 € ; score 77.12/100 ; SURVEILLE ; seuil achat non atteint
- DIA-EUR : 0.16392 € ; score 76.67/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- CTSI-EUR : 0.031848 € ; score 76.66/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017267 | +76.21 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.00902 | +57.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.058036 | +38.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.11918 | +34.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| W-EUR | 0.020153 | +27.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUMIA-EUR | 0.116233 | +24.45 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PLUME-EUR | 0.019978 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BAT-EUR | 0.1408 | +18.37 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IO-EUR | 0.16533 | +18.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.68868 | +17.42 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2143 scans ; 916953 observations ; 1657 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
