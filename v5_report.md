# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T23:28:40.224213+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-02T23:28:13.322614+00:00 | âge ticker : 148.2 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUPER-EUR : 0.20811 € ; score 92.68/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : 1.0822 € ; score 90.13/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.55 € ; score 88.23/100 ; SURVEILLE ; WICK_SETUP
- ILV-EUR : 3.5517 € ; score 88.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FLUID-EUR : 1.4234 € ; score 87.32/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.058798 | +47.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023255 | +15.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058714 | +12.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.088464 | +12.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.02975 | +11.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14609 | +10.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.022949 | +9.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.101131 | +8.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| WLD-EUR | 0.48462 | +8.35 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.53065 | +8.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2013 scans ; 861524 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
