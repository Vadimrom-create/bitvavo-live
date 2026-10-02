# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T13:29:47.376153+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 426
Récupération : 2026-10-02T13:29:20.617906+00:00 | âge ticker : 152.3 s | durée : 153.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AVNT-EUR : 0.11523 € ; score 89.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- APT-EUR : 0.751 € ; score 88.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SUI-EUR : 1.06809 € ; score 88.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.9592 € ; score 87.76/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : 2.2005 € ; score 86.51/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.060976 | +60.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.110281 | +27.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENJ-EUR | 0.032799 | +27.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.55532 | +23.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.092981 | +18.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GALA-EUR | 0.0023679 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20324 | +17.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.081363 | +16.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.7119 | +14.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SPK-EUR | 0.024006 | +14.12 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1981 scans ; 847892 observations ; 1564 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
