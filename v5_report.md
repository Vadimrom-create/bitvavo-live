# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T09:08:13.445056+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 33
Récupération : 2026-09-19T09:07:40.997412+00:00 | âge ticker : 152.9 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 73/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- JUP-EUR : INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INVALID_15M, INVALID_5M

## SURVEILLE

- TAO-EUR : 225.1 € ; score 89.61/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.63523 € ; score 85.95/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.35029 € ; score 79.15/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.108 € ; score 77.02/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.2886e-06 € ; score 76.75/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.223916 | +42.01 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.066763 | +40.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.15386 | +35.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.074886 | +29.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.30036 | +28.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.003611 | +25.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.046013 | +23.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022415 | +19.79 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EPIC-EUR | 0.37552 | +19.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.5665 | +18.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 876 scans ; 375831 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
