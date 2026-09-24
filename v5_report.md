# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T13:31:01.048568+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T13:30:35.646778+00:00 | âge ticker : 140.3 s | durée : 141.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KMNO-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- RAY-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.18812 € | IGNITION | score 87.79/100 | entrée 6.00/10
  Entrée 0.18844 € ; stop 0.17794 € ; TP1 0.20944 € ; TP2 0.21994 € ; montant 191.92 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 7.073/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ICP-EUR : 2.6818 € | IGNITION | score 87.27/100 | entrée 7.20/10
  Entrée 2.6818 € ; stop 2.5526 € ; TP1 2.9402 € ; TP2 3.0694 € ; montant 218.15 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.319/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KMNO-EUR : 0.032316 € ; score 93.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0080781 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.22166 € ; score 91.57/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- OP-EUR : 0.11235 € ; score 91.19/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.095159 € ; score 90.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021317 | +37.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.35154 | +27.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.099758 | +26.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.21956 | +15.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019573 | +13.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LTC-EUR | 61.345 | +12.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.41793 | +10.95 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.035343 | +10.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MORPHO-EUR | 2.50733 | +10.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.0852 | +8.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1358 scans ; 581245 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
