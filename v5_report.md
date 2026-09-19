# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T07:32:38.269977+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 30
Récupération : 2026-09-19T07:32:06.361713+00:00 | âge ticker : 146.4 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 67/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- AVAX-EUR : WICK_SETUP, INVALID_5M
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HYPE-EUR : 80.814 € ; score 81.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.15935 € ; score 77.27/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- PLUME-EUR : 0.0123804 € ; score 75.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- SOL-EUR : 97.234 € ; score 74.17/100 ; SURVEILLE ; WICK_SETUP
- APT-EUR : 0.6114 € ; score 74.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.088729 | +53.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.30343 | +30.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036913 | +28.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.046886 | +25.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.6102 | +25.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.200736 | +25.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.034439 | +25.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.140244 | +22.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.054724 | +20.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022165 | +17.53 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 870 scans ; 373269 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
