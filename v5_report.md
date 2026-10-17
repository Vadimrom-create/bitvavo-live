# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-17T06:04:50.202399+00:00
État : OK | marchés EUR : 427 | V4 : 372 | données valides : 427
Récupération : 2026-10-17T06:03:43.045928+00:00 | âge ticker : 191.1 s | durée : 192.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- INJ-EUR : 7.8836 € ; score 82.73/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- METIS-EUR : 3.6555 € ; score 75.21/100 ; SURVEILLE ; WIDE_SPREAD_RISK, WICK_SETUP
- RSR-EUR : 0.0017752 € ; score 74.53/100 ; SURVEILLE ; WICK_SETUP
- DODO-EUR : 0.019063 € ; score 73.94/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- KMNO-EUR : 0.036434 € ; score 72.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICNT-EUR | 0.17855 | +35.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.220496 | +26.37 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EPIC-EUR | 0.26599 | +25.47 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.66155 | +19.65 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EIGEN-EUR | 0.24612 | +11.14 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DUSK-EUR | 0.110906 | +8.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ELSA-EUR | 0.054801 | +8.44 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAD-EUR | 0.27271 | +7.82 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AMP-EUR | 0.0006353 | +7.19 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LIGHTER-EUR | 2.8928 | +6.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2178 scans ; 931898 observations ; 1659 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
