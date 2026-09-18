# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T23:41:49.748080+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 25
Récupération : 2026-09-18T23:41:19.526106+00:00 | âge ticker : 150.9 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/427 ; 15 min 74/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- FET-EUR : WICK_SETUP, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, EXTENDED_24H, CHASE_RISK, INVALID_5M

## SURVEILLE

- HYPE-EUR : 80.702 € ; score 82.05/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.3207e-06 € ; score 79.88/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0046088 | +64.79 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0066611 | +59.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038369 | +52.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19435 | +26.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.061939 | +25.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| APT-EUR | 0.6347 | +22.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044629 | +22.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZK-EUR | 0.009761 | +21.01 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYN-EUR | 0.198865 | +20.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.028091 | +19.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 841 scans ; 360886 observations ; 183 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
