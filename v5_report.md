# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T09:38:33.254132+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 32
Récupération : 2026-09-20T09:37:33.108195+00:00 | âge ticker : 179.3 s | durée : 180.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/426 ; 15 min 67/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M
- POL-EUR : WICK_SETUP, INVALID_5M

## SURVEILLE

- ONDO-EUR : 0.35892 € ; score 89.48/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 49.817 € ; score 86.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 79.16 € ; score 75.28/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.20608 € ; score 74.79/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0072066 € ; score 74.40/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0036061 | +76.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIL-EUR | 0.0035 | +26.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.026971 | +17.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SKL-EUR | 0.0040604 | +17.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.44086 | +13.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| T-EUR | 0.0046559 | +11.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SOLV-EUR | 0.0038843 | +10.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.5027 | +9.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.17931 | +9.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.27644 | +9.91 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 969 scans ; 415531 observations ; 225 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
