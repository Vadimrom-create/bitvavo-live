# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T15:02:27.825202+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T15:01:56.839341+00:00 | âge ticker : 162.1 s | durée : 163.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FIL-EUR : 0.98078 € ; score 89.93/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.44894 € ; score 89.60/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.089254 € ; score 88.74/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0038305 € ; score 87.68/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- FET-EUR : 0.20635 € ; score 87.67/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.30438 | +43.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.00169 | +33.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.002272 | +28.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.35984 | +25.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.62005 | +21.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.097628 | +20.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 153.44 | +19.69 % | DETECTED_EARLY | NONE | NONE |
| CELO-EUR | 0.095394 | +19.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ETHFI-EUR | 0.70971 | +18.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.1522 | +18.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1775 scans ; 759385 observations ; 1316 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
