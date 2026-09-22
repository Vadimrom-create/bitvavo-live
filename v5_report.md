# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T13:41:59.195532+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T13:41:34.353302+00:00 | âge ticker : 143.2 s | durée : 144.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WAL-EUR : 0.030093 € ; score 93.63/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- COW-EUR : 0.13777 € ; score 92.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- METIS-EUR : 3.0554 € ; score 90.13/100 ; SURVEILLE ; SPREAD_RISK
- ANIME-EUR : 0.0029583 € ; score 89.32/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.087259 € ; score 89.16/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01616 | +83.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014271 | +81.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.053221 | +28.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.071644 | +26.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XMN-EUR | 0.000515 | +23.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.28157 | +20.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.074453 | +17.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 273.92 | +17.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.37636 | +15.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.28e-06 | +15.64 % | DETECTED_EARLY | NONE | NONE |

Historique : 1189 scans ; 509251 observations ; 507 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
