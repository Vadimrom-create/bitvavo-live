# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T15:47:03.135794+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 34
Récupération : 2026-09-19T15:46:30.940202+00:00 | âge ticker : 146.8 s | durée : 147.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/427 ; 15 min 83/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INVALID_15M, INVALID_5M
- XPL-EUR : WICK_SETUP, INVALID_15M, INVALID_5M

## SURVEILLE

- PEPE-EUR : 3.3468e-06 € ; score 85.75/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.844 € ; score 81.49/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0073314 € ; score 80.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TAO-EUR : 235.43 € ; score 79.04/100 ; SURVEILLE ; seuil achat non atteint
- JUP-EUR : 0.24523 € ; score 78.60/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.070047 | +42.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.3191 | +33.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.206406 | +32.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.40958 | +28.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022207 | +23.90 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EDGE-EUR | 0.071675 | +22.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.080464 | +21.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17422 | +21.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.038231 | +20.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.28548 | +16.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 901 scans ; 386506 observations ; 207 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
