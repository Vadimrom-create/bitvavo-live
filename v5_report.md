# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T13:50:02.989835+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-24T13:49:35.959599+00:00 | âge ticker : 144.0 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : BELOW_EXCHANGE_MINIMUM
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.1128 € | IGNITION | score 89.43/100 | entrée 7.40/10
  Entrée 0.11238 € ; stop 0.10732 € ; TP1 0.12249 € ; TP2 0.12755 € ; montant 231.36 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.622/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- APT-EUR : 0.6958 € | IGNITION | score 88.95/100 | entrée 7.15/10
  Entrée 0.6968 € ; stop 0.6665 € ; TP1 0.7574 € ; TP2 0.7877 € ; montant 238.42 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- VET-EUR : 0.0080813 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DYM-EUR : 0.016141 € ; score 90.39/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- NEO-EUR : 2.2462 € ; score 90.27/100 ; SURVEILLE ; seuil achat non atteint
- ANIME-EUR : 0.002927 € ; score 89.89/100 ; SURVEILLE ; LOW_LIQUIDITY
- AUCTION-EUR : 3.3141 € ; score 89.23/100 ; SURVEILLE ; WIDE_SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0022115 | +43.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.364 | +32.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.098716 | +25.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.21694 | +14.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.42532 | +13.20 % | DETECTED_EARLY | NONE | NONE |
| MORPHO-EUR | 2.55578 | +12.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.085996 | +10.93 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| LTC-EUR | 60.795 | +10.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.15354 | +7.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28477 | +7.47 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1359 scans ; 581671 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
