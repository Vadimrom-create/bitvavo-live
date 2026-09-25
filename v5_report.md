# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T02:20:59.790635+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T02:20:26.837104+00:00 | âge ticker : 154.0 s | durée : 154.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- FLUX-EUR : 0.060452 € ; score 92.57/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 4.0698 € ; score 90.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.006923 € ; score 87.69/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ETC-EUR : 8.3371 € ; score 85.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- G-EUR : 0.0051237 € ; score 85.54/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.63193 | +28.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.4651 | +27.99 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 78.237 | +26.20 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098609 | +24.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAGA-EUR | 0.051254 | +20.61 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PEAQ-EUR | 0.03675 | +19.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16266 | +17.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.02125 | +16.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19898 | +15.65 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0081521 | +15.62 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1409 scans ; 603011 observations ; 795 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
