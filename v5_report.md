# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-22T00:14:22.178707+00:00
État : OK | marchés EUR : 428 | V4 : 365 | données valides : 428
Récupération : 2026-10-22T00:13:18.182189+00:00 | âge ticker : 177.1 s | durée : 177.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.52272 € ; score 81.97/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- METIS-EUR : 3.7467 € ; score 78.08/100 ; SURVEILLE ; seuil achat non atteint
- CTR-EUR : 0.013578 € ; score 76.42/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.037411 € ; score 75.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WAL-EUR : 0.035381 € ; score 73.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| IRYS-EUR | 0.016528 | +37.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ALT-EUR | 0.011852 | +33.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BILL-EUR | 0.006528 | +29.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PROM-EUR | 5.2535 | +18.74 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| DYM-EUR | 0.018024 | +14.00 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRIA-EUR | 0.002485 | +13.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IOST-EUR | 0.0010703 | +13.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PARTI-EUR | 0.029458 | +12.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LIGHTER-EUR | 3.3925 | +12.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ORCA-EUR | 1.76793 | +11.54 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2209 scans ; 945137 observations ; 1661 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
