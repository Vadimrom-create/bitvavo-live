# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T18:58:50.024311+00:00
État : OK | marchés EUR : 426 | V4 : 410 | données valides : 426
Récupération : 2026-09-23T18:57:40.845533+00:00 | âge ticker : 189.3 s | durée : 190.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TRAC-EUR : 0.30596 € ; score 88.32/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- DATAIP-EUR : 0.196 € ; score 86.89/100 ; SURVEILLE ; seuil achat non atteint
- HNT-EUR : 0.43095 € ; score 86.17/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- LTC-EUR : 53.74 € ; score 85.07/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYN-EUR : 0.18514 € ; score 83.26/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.044952 | +37.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.031167 | +28.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018277 | +26.55 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NIL-EUR | 0.087756 | +22.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.86212 | +20.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.1566 | +17.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.7817 | +13.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30608 | +13.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3484 | +12.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COTI-EUR | 0.014735 | +10.36 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1290 scans ; 552277 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
