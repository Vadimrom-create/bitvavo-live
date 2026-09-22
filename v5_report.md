# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T05:47:57.097425+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T05:47:27.899409+00:00 | âge ticker : 146.3 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MERL-EUR : 0.024386 € ; score 94.03/100 ; SURVEILLE ; seuil achat non atteint
- T-EUR : 0.0045525 € ; score 89.28/100 ; SURVEILLE ; SPREAD_RISK
- CC-EUR : 0.103 € ; score 88.64/100 ; SURVEILLE ; seuil achat non atteint
- LIGHTER-EUR : 4.241 € ; score 88.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- STO-EUR : 0.036277 € ; score 86.13/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014874 | +91.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015738 | +81.56 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.12485 | +57.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057811 | +32.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.4455e-06 | +26.89 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.38652 | +22.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27486 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.2121 | +21.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TAO-EUR | 278.19 | +18.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.036247 | +17.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1153 scans ; 493915 observations ; 461 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
