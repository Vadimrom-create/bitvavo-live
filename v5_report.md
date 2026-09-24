# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T05:03:19.954807+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-24T05:02:52.030723+00:00 | âge ticker : 154.8 s | durée : 156.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VET-EUR : 0.0079862 € ; score 91.48/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034363 € ; score 90.71/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.5633 € ; score 90.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.8807e-06 € ; score 90.07/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.17552 € ; score 89.94/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.121858 | +39.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020507 | +32.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.31572 | +16.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.018845 | +15.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.00194 | +14.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RAY-EUR | 1.7962 | +13.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.028088 | +11.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.3712 | +11.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.2866 | +9.06 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CPOOL-EUR | 0.028793 | +8.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1330 scans ; 569317 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
