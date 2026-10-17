# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-17T01:32:09.526731+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-10-17T01:31:05.067536+00:00 | âge ticker : 176.5 s | durée : 177.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- INJ-EUR : 7.7273 € ; score 83.97/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EDU-EUR : 0.06863 € ; score 76.03/100 ; SURVEILLE ; seuil achat non atteint
- MEGA-EUR : 0.04329 € ; score 75.07/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.034828 € ; score 75.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RSR-EUR : 0.0017 € ; score 74.09/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICNT-EUR | 0.17067 | +31.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TIA-EUR | 0.61236 | +15.84 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AMP-EUR | 0.0006738 | +15.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DUSK-EUR | 0.109676 | +13.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| METIS-EUR | 3.705 | +10.27 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAD-EUR | 0.2754 | +10.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MEGA-EUR | 0.04329 | +8.17 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PHA-EUR | 0.0482 | +7.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CTR-EUR | 0.012392 | +6.91 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RECALL-EUR | 0.03529 | +6.76 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2177 scans ; 931471 observations ; 1659 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
