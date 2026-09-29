# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T14:22:31.581765+00:00
État : OK | marchés EUR : 429 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T14:22:00.330257+00:00 | âge ticker : 156.4 s | durée : 157.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.4208 € | IGNITION | score 87.05/100 | entrée 7.65/10
  Entrée 4.4235 € ; stop 4.2042 € ; TP1 4.862 € ; TP2 5.0813 € ; montant 212.76 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 2.922/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0020577 € ; score 87.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- APE-EUR : 0.1353 € ; score 86.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.44427 € ; score 84.32/100 ; SURVEILLE ; seuil achat non atteint
- FLR-EUR : 0.0066143 € ; score 83.51/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.46 € ; score 82.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.31476 | +44.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0017 | +36.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022246 | +25.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELO-EUR | 0.098568 | +22.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.3525 | +20.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.22127 | +18.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 153.15 | +17.17 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.62259 | +16.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICP-EUR | 3.0482 | +16.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.0203 | +14.69 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1773 scans ; 758527 observations ; 1315 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
