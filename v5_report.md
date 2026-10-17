# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-17T10:30:56.205972+00:00
État : OK | marchés EUR : 427 | V4 : 371 | données valides : 427
Récupération : 2026-10-17T10:29:50.948402+00:00 | âge ticker : 178.0 s | durée : 179.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- INJ-EUR : 7.7977 € ; score 79.81/100 ; SURVEILLE ; seuil achat non atteint
- METIS-EUR : 3.6649 € ; score 76.24/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- FLUID-EUR : 2.1235 € ; score 72.47/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.038431 € ; score 72.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KMNO-EUR : 0.037635 € ; score 72.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICNT-EUR | 0.1754 | +43.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.24379 | +24.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GTC-EUR | 0.21284 | +21.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AVA-EUR | 0.27783 | +12.45 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| THQ-EUR | 0.009951 | +8.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| METIS-EUR | 3.6649 | +8.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KMNO-EUR | 0.037635 | +7.92 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRC-EUR | 0.0013823 | +6.71 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RECALL-EUR | 0.035329 | +6.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SAND-EUR | 0.0518 | +6.20 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2179 scans ; 932325 observations ; 1660 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
