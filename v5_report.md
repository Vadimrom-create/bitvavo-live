# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T11:42:37.272764+00:00
État : OK | marchés EUR : 429 | V4 : 396 | données valides : 428
Récupération : 2026-09-29T11:42:05.947406+00:00 | âge ticker : 152.7 s | durée : 155.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RUNE-EUR : 0.69464 € ; score 92.81/100 ; SURVEILLE ; WICK_SETUP
- CC-EUR : 0.11484 € ; score 88.97/100 ; SURVEILLE ; WICK_SETUP
- XPL-EUR : 0.089398 € ; score 88.80/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72198 € ; score 88.38/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0165932 € ; score 88.15/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019471 | +56.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CELO-EUR | 0.10266 | +28.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.28357 | +28.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.60405 | +21.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.22077 | +19.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.34499 | +18.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0021183 | +18.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 150.8 | +15.58 % | DETECTED_EARLY | NONE | NONE |
| CVX-EUR | 2.0425 | +15.40 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.088264 | +14.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1766 scans ; 755524 observations ; 1307 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
