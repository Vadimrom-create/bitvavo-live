# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T02:22:16.600615+00:00
État : OK | marchés EUR : 426 | V4 : 362 | données valides : 426
Récupération : 2026-10-04T02:21:09.622995+00:00 | âge ticker : 182.1 s | durée : 182.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 161.54 € ; score 82.58/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.52203 € ; score 78.44/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.22783 € ; score 74.47/100 ; SURVEILLE ; WICK_SETUP
- SKY-EUR : 0.080889 € ; score 74.39/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.030302 € ; score 74.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GLMR-EUR | 0.01092 | +44.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.120969 | +32.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TREAD-EUR | 1.02142 | +25.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| HFT-EUR | 0.00697 | +22.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FUN-EUR | 0.019094 | +21.81 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.04693 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.079842 | +17.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MERL-EUR | 0.028918 | +15.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZRO-EUR | 1.8269 | +14.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0055567 | +12.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2050 scans ; 877286 observations ; 1627 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
