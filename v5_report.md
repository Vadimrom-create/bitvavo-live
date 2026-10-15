# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-15T01:00:43.426416+00:00
État : OK | marchés EUR : 427 | V4 : 374 | données valides : 427
Récupération : 2026-10-15T00:59:30.982884+00:00 | âge ticker : 199.0 s | durée : 200.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- ICNT-EUR : 0.09805 € ; score 83.32/100 ; SURVEILLE ; WICK_SETUP
- OP-EUR : 0.12621 € ; score 81.56/100 ; SURVEILLE ; seuil achat non atteint
- TRAC-EUR : 0.39261 € ; score 77.30/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.013911 € ; score 74.61/100 ; SURVEILLE ; seuil achat non atteint
- AXL-EUR : 0.051281 € ; score 73.90/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| WAL-EUR | 0.050078 | +38.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OSMO-EUR | 0.043836 | +19.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009621 | +14.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.035593 | +12.49 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.077684 | +12.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AVA-EUR | 0.24297 | +11.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DEEP-EUR | 0.021089 | +11.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.001585 | +10.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PYTH-EUR | 0.0745 | +5.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LAPTOP-EUR | 0.07114 | +4.76 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2164 scans ; 925920 observations ; 1658 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
