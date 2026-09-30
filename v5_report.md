# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T08:40:25.212884+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T08:39:50.066200+00:00 | âge ticker : 151.7 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.0159821 € ; score 92.11/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.11258 € ; score 90.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.3856e-06 € ; score 87.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEAR-EUR : 4.4571 € ; score 84.62/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.21842 € ; score 84.03/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5948 | +83.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.102694 | +34.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.071947 | +24.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GLMR-EUR | 0.008243 | +23.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.38781 | +21.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.25469 | +17.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.30115 | +16.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022354 | +15.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00048427 | +15.01 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0050679 | +14.79 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1828 scans ; 782122 observations ; 1364 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
