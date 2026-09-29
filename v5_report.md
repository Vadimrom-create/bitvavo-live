# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T13:38:58.817765+00:00
État : OK | marchés EUR : 429 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T13:38:22.360319+00:00 | âge ticker : 155.5 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CFG-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ENA-EUR : 0.22601 € ; score 92.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : 0.0047883 € ; score 88.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BRETT-EUR : 0.0051076 € ; score 86.53/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- SKY-EUR : 0.073831 € ; score 85.33/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.039164 € ; score 84.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.30252 | +36.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016418 | +32.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0021685 | +21.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELO-EUR | 0.09961 | +20.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.35385 | +20.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0963 | +18.38 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYRUP-EUR | 0.22258 | +17.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.63188 | +15.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 152.94 | +15.46 % | DETECTED_EARLY | NONE | NONE |
| EDEN-EUR | 0.058756 | +13.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1771 scans ; 757669 observations ; 1313 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
