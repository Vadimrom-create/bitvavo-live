# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T05:58:39.688793+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 27
Récupération : 2026-09-19T05:57:34.511481+00:00 | âge ticker : 184.7 s | durée : 185.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/427 ; 15 min 65/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XRP-EUR : 1.24137 € ; score 85.02/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 123.76 € ; score 84.05/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 97.762 € ; score 79.37/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 221.46 € ; score 78.21/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.047 € ; score 77.85/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0067238 | +55.35 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EDGE-EUR | 0.083431 | +46.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.035183 | +30.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0037114 | +29.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.28798 | +26.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.024697 | +21.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022926 | +21.10 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053569 | +21.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.192618 | +20.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044758 | +19.78 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 865 scans ; 371134 observations ; 189 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
