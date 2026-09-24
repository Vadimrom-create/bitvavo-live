# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T14:25:02.985555+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-09-24T14:24:36.233629+00:00 | âge ticker : 144.0 s | durée : 144.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : BELOW_EXCHANGE_MINIMUM
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : BELOW_EXCHANGE_MINIMUM
- FET-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- PEPE-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- PYTH-EUR : BELOW_EXCHANGE_MINIMUM
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : BELOW_EXCHANGE_MINIMUM
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : BELOW_EXCHANGE_MINIMUM
- XLM-EUR : BELOW_EXCHANGE_MINIMUM
- HBAR-EUR : 0.0824 € | IGNITION | score 91.55/100 | entrée 8.05/10
  Entrée 0.0824 € ; stop 0.078895 € ; TP1 0.089409 € ; TP2 0.092914 € ; montant 242.98 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.846/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.21633 € | IGNITION | score 91.51/100 | entrée 8.05/10
  Entrée 0.21646 € ; stop 0.2063 € ; TP1 0.23678 € ; TP2 0.24694 € ; montant 223.16 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.466/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- UNI-EUR : 8.1078 € ; score 91.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034553 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.9091e-06 € ; score 91.05/100 ; SURVEILLE ; WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- MMT-EUR : 0.15139 € ; score 90.59/100 ; SURVEILLE ; LOW_LIQUIDITY
- TRB-EUR : 17.67 € ; score 90.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0020962 | +41.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.101231 | +34.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.34831 | +31.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44531 | +23.22 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 64.899 | +23.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0157602 | +16.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MORPHO-EUR | 2.563 | +15.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.2148 | +15.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ETC-EUR | 8.9169 | +15.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.1548 | +12.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1361 scans ; 582523 observations ; 717 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
