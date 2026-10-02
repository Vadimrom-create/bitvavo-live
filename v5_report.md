# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T16:43:55.185052+00:00
État : OK | marchés EUR : 426 | V4 : 390 | données valides : 426
Récupération : 2026-10-02T16:43:23.292200+00:00 | âge ticker : 149.1 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AZTEC-EUR : 0.015601 € ; score 91.60/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 163.04 € ; score 88.06/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DBR-EUR : 0.016966 € ; score 85.79/100 ; SURVEILLE ; seuil achat non atteint
- HUMA-EUR : 0.030057 € ; score 84.78/100 ; SURVEILLE ; seuil achat non atteint
- DYDX-EUR : 0.13794 € ; score 84.70/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.055767 | +44.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.124048 | +32.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.082944 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0059637 | +15.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023108 | +15.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.50266 | +15.59 % | DETECTED_EARLY | NONE | NONE |
| SUPER-EUR | 0.20727 | +14.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.56061 | +13.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089007 | +12.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.7438 | +12.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1990 scans ; 851726 observations ; 1573 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
