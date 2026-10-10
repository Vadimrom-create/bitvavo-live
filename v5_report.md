# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-10T20:45:19.109995+00:00
État : OK | marchés EUR : 427 | V4 : 378 | données valides : 427
Récupération : 2026-10-10T20:44:10.123205+00:00 | âge ticker : 184.5 s | durée : 185.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- FLUX-EUR : 0.075952 € ; score 75.52/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- STX-EUR : 0.36408 € ; score 75.31/100 ; SURVEILLE ; WICK_SETUP
- IMX-EUR : 0.1769 € ; score 75.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- APT-EUR : 0.7697 € ; score 74.93/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- S-EUR : 0.041917 € ; score 74.11/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| STRK-EUR | 0.091354 | +47.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHIP-EUR | 0.05965 | +32.36 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LUMIA-EUR | 0.0934 | +29.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.51635 | +23.43 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AZTEC-EUR | 0.015452 | +16.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AERO-EUR | 0.82327 | +15.45 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NEAR-EUR | 4.7957 | +15.05 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| WLD-EUR | 0.50397 | +13.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DUSK-EUR | 0.078773 | +12.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0810345 | +12.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2133 scans ; 912683 observations ; 1656 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
