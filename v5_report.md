# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T15:01:23.261659+00:00
État : OK | marchés EUR : 426 | V4 : 390 | données valides : 426
Récupération : 2026-09-24T15:00:52.486761+00:00 | âge ticker : 151.0 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- FLOKI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.2175 € | IGNITION | score 89.50/100 | entrée 7.20/10
  Entrée 0.21682 € ; stop 0.20708 € ; TP1 0.2363 € ; TP2 0.24604 € ; montant 231.82 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.066/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- JUP-EUR : 0.26121 € ; score 91.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MEW-EUR : 0.0004214 € ; score 90.85/100 ; SURVEILLE ; LOW_LIQUIDITY
- WAL-EUR : 0.029268 € ; score 90.59/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.21572 € ; score 89.17/100 ; SURVEILLE ; CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- CAKE-EUR : 2.3591 € ; score 89.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.002034 | +35.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.33946 | +25.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.099626 | +24.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LTC-EUR | 63.874 | +19.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.43788 | +18.86 % | DETECTED_EARLY | NONE | NONE |
| ARX-EUR | 0.22019 | +15.46 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PEAQ-EUR | 0.034579 | +14.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0154475 | +12.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 70.544 | +12.29 % | DETECTED_EARLY | NONE | NONE |
| ETC-EUR | 8.6212 | +9.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1363 scans ; 583375 observations ; 717 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
