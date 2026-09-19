# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T15:19:15.097339+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 33
Récupération : 2026-09-19T15:18:45.830230+00:00 | âge ticker : 145.3 s | durée : 146.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INVALID_5M
- POL-EUR : STABILITY_HOLD, INVALID_5M
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HYPE-EUR : 81.23 € ; score 92.50/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 236.89 € ; score 84.48/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.241506 € ; score 82.29/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 97.402 € ; score 76.51/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : 71091 € ; score 74.77/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.069252 | +41.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.33098 | +39.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.203696 | +31.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.40714 | +27.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022639 | +27.83 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.037968 | +24.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.071001 | +20.89 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.0806 | +20.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17153 | +19.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.2035 | +16.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 899 scans ; 385652 observations ; 204 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
