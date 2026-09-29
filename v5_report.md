# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T23:06:40.929526+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T23:05:40.114361+00:00 | âge ticker : 173.9 s | durée : 174.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZRO-EUR : 1.482 € | IGNITION | score 87.88/100 | entrée 5.90/10
  Entrée 1.4847 € ; stop 1.3963 € ; TP1 1.6614 € ; TP2 1.7498 € ; montant 180.91 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 6.164/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DATAIP-EUR : 0.198 € ; score 90.15/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.012254 € ; score 89.28/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.007944 € ; score 85.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEGA-EUR : 0.03718 € ; score 83.84/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP, STABILITY_HOLD
- JASMY-EUR : 0.0046378 € ; score 81.89/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017233 | +36.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66959 | +30.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0568 | +25.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.065231 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0021781 | +22.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.36201 | +21.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0052159 | +21.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29032 | +16.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 232.814 | +14.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRIA-EUR | 0.003989 | +13.84 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1800 scans ; 770110 observations ; 1340 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
