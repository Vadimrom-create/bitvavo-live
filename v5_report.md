# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T16:04:14.877127+00:00
État : OK | marchés EUR : 429 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T16:03:36.061349+00:00 | âge ticker : 159.1 s | durée : 160.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- PLUME-EUR : 0.0159843 € ; score 91.01/100 ; SURVEILLE ; WICK_SETUP
- ATH-EUR : 0.0053435 € ; score 90.00/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.6926 € ; score 89.46/100 ; SURVEILLE ; seuil achat non atteint
- EGLD-EUR : 4.0278 € ; score 88.53/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- MET-EUR : 0.27858 € ; score 86.35/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.29684 | +36.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0017088 | +35.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022899 | +29.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.60301 | +25.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.097545 | +21.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.35218 | +20.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDP-EUR | 0.021779 | +17.29 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AAVE-EUR | 149.89 | +16.86 % | DETECTED_EARLY | NONE | NONE |
| SYRUP-EUR | 0.21613 | +16.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.34356 | +15.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1778 scans ; 760672 observations ; 1321 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
