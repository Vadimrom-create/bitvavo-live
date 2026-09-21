# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T08:04:40.475341+00:00
État : OK | marchés EUR : 426 | V4 : 377 | données valides : 426
Récupération : 2026-09-21T08:04:08.129495+00:00 | âge ticker : 148.8 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MERL-EUR : 0.023509 € ; score 94.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- OP-EUR : 0.11016 € ; score 88.88/100 ; SURVEILLE ; seuil achat non atteint
- KITE-EUR : 0.10196 € ; score 85.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TAO-EUR : 237.91 € ; score 85.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WOO-EUR : 0.01055 € ; score 84.72/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.054797 | +65.02 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009531 | +57.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.24895 | +36.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.058397 | +35.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.032461 | +34.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.51315 | +25.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029321 | +24.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 29.5207 | +22.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.7084 | +21.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.04965 | +19.50 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1058 scans ; 453445 observations ; 330 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
