# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T03:44:34.306121+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T03:44:01.139252+00:00 | âge ticker : 146.2 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALICE-EUR : 0.15981 € ; score 90.93/100 ; SURVEILLE ; seuil achat non atteint
- SLP-EUR : 0.00064039 € ; score 85.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PARTI-EUR : 0.024767 € ; score 85.13/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ORCA-EUR : 1.58721 € ; score 83.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- C-EUR : 0.085691 € ; score 83.71/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.071649 | +80.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.095553 | +21.01 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.031912 | +18.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.00595 | +13.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023067 | +13.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.49544 | +13.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.15097 | +12.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1432 | +12.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.08871 | +11.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| WLD-EUR | 0.50271 | +10.54 % | DETECTED_EARLY | NONE | NONE |

Historique : 2025 scans ; 866636 observations ; 1594 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
