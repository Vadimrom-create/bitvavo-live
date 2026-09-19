# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T16:00:12.971896+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 33
Récupération : 2026-09-19T15:59:37.819164+00:00 | âge ticker : 159.8 s | durée : 160.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/427 ; 15 min 83/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- XPL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M

## SURVEILLE

- PEPE-EUR : 3.3425e-06 € ; score 90.10/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.944 € ; score 85.16/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0035691 € ; score 82.56/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0073288 € ; score 80.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TAO-EUR : 235.56 € ; score 76.27/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.073647 | +47.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.32516 | +36.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.206779 | +31.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.40771 | +28.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.02199 | +22.69 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AIOZ-EUR | 0.07992 | +19.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17313 | +19.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.038417 | +18.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0088373 | +18.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.068997 | +17.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 902 scans ; 386933 observations ; 210 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
