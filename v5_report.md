# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T07:41:30.329907+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-22T07:41:01.989316+00:00 | âge ticker : 147.0 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ALGO-EUR : 0.097023 € ; score 92.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MANA-EUR : 0.0753 € ; score 91.62/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.1452 € ; score 90.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DOGS-EUR : 4.4225e-05 € ; score 87.86/100 ; SURVEILLE ; seuil achat non atteint
- ARPA-EUR : 0.009436 € ; score 87.48/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017113 | +103.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015598 | +100.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.11918 | +46.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.059616 | +44.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5094e-06 | +29.18 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21908 | +24.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39045 | +22.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27274 | +20.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.248523 | +19.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FARTCOIN-EUR | 0.1755 | +18.98 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1162 scans ; 497749 observations ; 466 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
