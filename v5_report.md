# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T04:03:45.163105+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T04:02:47.462211+00:00 | âge ticker : 173.7 s | durée : 174.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.082247 € | IGNITION | score 88.59/100 | entrée 7.85/10
  Entrée 0.082265 € ; stop 0.079097 € ; TP1 0.088601 € ; TP2 0.091769 € ; montant 250.00 € ; risque théorique 11.34 € ; R/R net 1.54.
  Chase risk : 1.939/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAIKO-EUR : 0.08117 € ; score 91.41/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MMT-EUR : 0.14523 € ; score 88.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- YGG-EUR : 0.022966 € ; score 88.43/100 ; SURVEILLE ; LOW_LIQUIDITY
- PYTH-EUR : 0.056148 € ; score 87.44/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TOSHI-EUR : 0.00011354 € ; score 87.44/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016174 | +87.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.001329 | +71.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.056522 | +47.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.113123 | +41.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.047828 | +40.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.5876e-06 | +31.31 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.221 | +24.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27539 | +20.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CARV-EUR | 0.040127 | +19.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FARTCOIN-EUR | 0.17571 | +18.47 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1147 scans ; 491359 observations ; 451 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
