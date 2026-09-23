# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T09:17:57.845393+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T09:17:26.334435+00:00 | âge ticker : 149.1 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XVG-EUR : 0.0027344 € ; score 89.64/100 ; SURVEILLE ; seuil achat non atteint
- MOVR-EUR : 0.8342 € ; score 88.14/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- ICNT-EUR : 0.08868 € ; score 85.73/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.058547 € ; score 85.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.063954 € ; score 84.89/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.0367 | +48.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.33475 | +34.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 309.37 | +32.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.17436 | +31.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.0865 | +27.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019522 | +27.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.289671 | +24.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2707 | +23.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.46144 | +20.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.009559 | +20.09 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1258 scans ; 538645 observations ; 633 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
