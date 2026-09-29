# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T09:47:58.000015+00:00
État : OK | marchés EUR : 428 | V4 : 394 | données valides : 428
Récupération : 2026-09-29T09:47:24.428805+00:00 | âge ticker : 147.8 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- JUP-EUR : 0.29246 € ; score 90.88/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.44905 € ; score 89.85/100 ; SURVEILLE ; SPREAD_RISK
- IMX-EUR : 0.15266 € ; score 88.11/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XDC-EUR : 0.031526 € ; score 86.46/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- RARE-EUR : 0.015256 € ; score 85.08/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018147 | +46.42 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.1326 | +28.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.61585 | +23.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35244 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 225.859 | +23.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21871 | +21.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.069 | +18.32 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.08915 | +18.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.2606 | +16.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.305 | +15.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1760 scans ; 752953 observations ; 1287 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
