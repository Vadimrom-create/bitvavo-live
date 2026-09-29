# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T07:42:38.399078+00:00
État : OK | marchés EUR : 428 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T07:42:11.212356+00:00 | âge ticker : 151.7 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- FET-EUR : SPREAD_RISK, STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- GALA-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEAQ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : BELOW_EXCHANGE_MINIMUM
- UNI-EUR : BELOW_EXCHANGE_MINIMUM
- VIRTUAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : 0.461 € | IGNITION | score 89.69/100 | entrée 7.50/10
  Entrée 0.46107 € ; stop 0.44061 € ; TP1 0.50198 € ; TP2 0.52244 € ; montant 234.28 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 2.472/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.44211 € | IGNITION | score 88.78/100 | entrée 7.60/10
  Entrée 0.44211 € ; stop 0.41326 € ; TP1 0.49981 € ; TP2 0.52865 € ; montant 166.60 € ; risque théorique 12.00 € ; R/R net 1.71.
  Chase risk : 6.06/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KMNO-EUR : 0.038796 € ; score 90.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PLUME-EUR : 0.0159378 € ; score 89.17/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.22181 € ; score 87.66/100 ; SURVEILLE ; WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- TAO-EUR : 276.32 € ; score 87.55/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- UNI-EUR : 7.8531 € ; score 87.55/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.1539 | +30.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35021 | +22.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.25191 | +21.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0014931 | +21.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.103401 | +20.19 % | DETECTED_EARLY | NONE | NONE |
| CELO-EUR | 0.092563 | +16.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.61199 | +15.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.25806 | +15.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.14832 | +14.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.049512 | +13.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1754 scans ; 750385 observations ; 1284 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
