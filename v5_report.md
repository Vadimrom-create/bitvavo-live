# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T14:43:52.444942+00:00
État : OK | marchés EUR : 429 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T14:42:55.866915+00:00 | âge ticker : 181.4 s | durée : 182.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.45658 € | IGNITION | score 92.39/100 | entrée 7.60/10
  Entrée 0.45638 € ; stop 0.4348 € ; TP1 0.49954 € ; TP2 0.52112 € ; montant 221.73 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 1.027/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 4.4255 € | IGNITION | score 90.93/100 | entrée 7.60/10
  Entrée 4.4199 € ; stop 4.2 € ; TP1 4.8597 € ; TP2 5.0796 € ; montant 212.10 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.592/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COMP-EUR : 22.213 € ; score 92.40/100 ; SURVEILLE ; WICK_SETUP
- AERO-EUR : 0.71941 € ; score 91.63/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0028667 € ; score 91.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- XPL-EUR : 0.08916 € ; score 90.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012532 € ; score 89.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.307 | +44.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.00177 | +42.74 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022734 | +30.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.35592 | +24.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.095734 | +20.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 155.19 | +20.49 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.61445 | +19.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ETHFI-EUR | 0.71305 | +19.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21908 | +17.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0283 | +17.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1774 scans ; 758956 observations ; 1316 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
