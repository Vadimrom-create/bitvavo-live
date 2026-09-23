# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T14:06:11.579265+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-23T14:05:38.081781+00:00 | âge ticker : 150.8 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : 2.7367 € | IGNITION | score 83.80/100 | entrée 7.00/10
  Entrée 2.7431 € ; stop 2.6436 € ; TP1 2.9421 € ; TP2 3.0416 € ; montant 250.00 € ; risque théorique 10.79 € ; R/R net 1.51.
  Chase risk : 2.189/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MIRA-EUR : 0.048802 € ; score 92.70/100 ; SURVEILLE ; LOW_LIQUIDITY
- ZBT-EUR : 0.079346 € ; score 92.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ORCA-EUR : 1.3828 € ; score 92.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZEN-EUR : 7.1723 € ; score 90.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ARX-EUR : 0.19089 € ; score 90.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034039 | +39.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.309709 | +36.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.32994 | +30.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.0415 | +24.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020707 | +22.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16236 | +21.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.18024 | +20.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2969 | +18.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.017084 | +18.20 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| LIGHTER-EUR | 4.785 | +16.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1274 scans ; 545461 observations ; 652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
