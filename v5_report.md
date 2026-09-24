# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T22:52:50.817661+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T22:52:19.399981+00:00 | âge ticker : 151.4 s | durée : 152.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.2007 € ; score 92.00/100 ; SURVEILLE ; WICK_SETUP
- BABY-EUR : 0.011255 € ; score 88.71/100 ; SURVEILLE ; WICK_SETUP
- MAGIC-EUR : 0.043545 € ; score 87.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZBT-EUR : 0.077018 € ; score 86.25/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- PROM-EUR : 4.8908 € ; score 84.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.059985 | +42.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.039466 | +27.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 78.971 | +27.00 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0087509 | +26.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.022173 | +26.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.45715 | +25.60 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.59503 | +24.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.171 | +22.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.096546 | +21.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.36825 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1397 scans ; 597887 observations ; 768 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
