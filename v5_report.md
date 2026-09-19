# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T08:00:11.153389+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 33
Récupération : 2026-09-19T07:59:08.107801+00:00 | âge ticker : 182.9 s | durée : 183.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 39/427 ; 15 min 67/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INVALID_15M, INVALID_5M
- RAY-EUR : INVALID_15M, INVALID_5M

## SURVEILLE

- AVAX-EUR : 7.4532 € ; score 88.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- USDC-EUR : 0.8689 € ; score 80.71/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.719 € ; score 76.99/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 97.033 € ; score 76.20/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.1668 € ; score 76.20/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.087638 | +51.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0037949 | +31.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.30612 | +31.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.208789 | +30.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.14628 | +28.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.047011 | +25.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.5965 | +22.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.37816 | +19.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.035061 | +19.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022349 | +18.46 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 872 scans ; 374123 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
