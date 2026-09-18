# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T23:47:21.737148+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 25
Récupération : 2026-09-18T23:46:50.737351+00:00 | âge ticker : 146.0 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/427 ; 15 min 74/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PEPE-EUR : 3.3196e-06 € ; score 79.02/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.667 € ; score 78.48/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.14675 € ; score 77.01/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.34678 € ; score 72.25/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0045932 | +64.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0066309 | +59.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038245 | +51.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19596 | +26.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.061712 | +24.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044657 | +22.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6339 | +21.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZK-EUR | 0.009761 | +21.01 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.53563 | +19.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028091 | +19.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 842 scans ; 361313 observations ; 183 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
