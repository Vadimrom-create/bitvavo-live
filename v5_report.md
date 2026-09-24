# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T03:22:41.771706+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T03:21:45.903786+00:00 | âge ticker : 176.7 s | durée : 177.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 7.9971 € | IGNITION | score 91.90/100 | entrée 6.95/10
  Entrée 8.0023 € ; stop 7.6071 € ; TP1 8.7927 € ; TP2 9.1878 € ; montant 213.47 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 6.102/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- A-EUR : 0.081655 € ; score 91.19/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.010158 € ; score 90.73/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- VET-EUR : 0.007874 € ; score 90.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.6096 € ; score 90.18/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.268346 € ; score 89.48/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.124341 | +36.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0020291 | +30.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.040366 | +14.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.4245 | +13.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018455 | +12.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.02873 | +11.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.30038 | +9.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.033277 | +9.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.2881 | +8.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RAY-EUR | 1.76846 | +7.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1324 scans ; 566761 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
