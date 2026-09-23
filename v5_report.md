# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T01:00:48.645892+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-23T01:00:19.015699+00:00 | âge ticker : 152.6 s | durée : 153.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BNB-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- F-EUR : 0.0033052 € ; score 88.00/100 ; SURVEILLE ; LOW_LIQUIDITY
- VTHO-EUR : 0.00062076 € ; score 84.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- CAKE-EUR : 2.2548 € ; score 82.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- ETC-EUR : 8.2463 € ; score 82.19/100 ; SURVEILLE ; WICK_SETUP
- THE-EUR : 0.07239 € ; score 81.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BCH-EUR | 298.28 | +28.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.075026 | +25.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.05387 | +25.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018447 | +22.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.018865 | +21.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.300225 | +20.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MLN-EUR | 1.4586 | +20.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MET-EUR | 0.29247 | +19.32 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FLOCK-EUR | 0.075926 | +18.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.44092 | +16.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1230 scans ; 526717 observations ; 565 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
