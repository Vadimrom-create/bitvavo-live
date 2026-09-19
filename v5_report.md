# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T00:11:48.705932+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 25
Récupération : 2026-09-19T00:11:19.195814+00:00 | âge ticker : 143.6 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/427 ; 15 min 70/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- FET-EUR : WICK_SETUP, INVALID_5M
- KAS-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAO-EUR : 219.21 € ; score 82.62/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 50.763 € ; score 81.51/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.314e-06 € ; score 79.04/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.436 € ; score 75.01/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- ONDO-EUR : 0.34724 € ; score 72.16/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0044339 | +58.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0064724 | +54.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037672 | +49.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19405 | +25.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6434 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.060816 | +23.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044392 | +21.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024772 | +20.86 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| OP-EUR | 0.10523 | +19.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.052226 | +19.60 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 844 scans ; 362167 observations ; 184 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
