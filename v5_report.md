# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T18:41:54.322031+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T18:41:20.635324+00:00 | âge ticker : 153.7 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ADA-EUR : 0.21257 € ; score 85.37/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 53.685 € ; score 85.03/100 ; SURVEILLE ; seuil achat non atteint
- PNUT-EUR : 0.049306 € ; score 85.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LPT-EUR : 1.5154 € ; score 84.52/100 ; SURVEILLE ; seuil achat non atteint
- STO-EUR : 0.03592 € ; score 83.16/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.001839 | +137.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016164 | +91.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053312 | +58.42 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31558 | +41.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043946 | +38.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010265 | +30.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3806e-06 | +25.65 % | DETECTED_EARLY | NONE | NONE |
| AIOZ-EUR | 0.098481 | +24.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008075 | +24.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21292 | +21.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1100 scans ; 471337 observations ; 401 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
