# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T00:53:09.126187+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 23
Récupération : 2026-09-19T00:52:41.554371+00:00 | âge ticker : 144.8 s | durée : 145.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/427 ; 15 min 65/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INVALID_5M
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INVALID_5M
- ONDO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INVALID_5M
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INVALID_5M
- W-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- XLM-EUR : WICK_SETUP, INVALID_5M
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.0125317 € ; score 84.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XRP-EUR : 1.22837 € ; score 82.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 81.205 € ; score 81.80/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.34965 € ; score 79.66/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.16058 € ; score 77.48/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0044728 | +59.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0063371 | +53.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.036997 | +46.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053946 | +23.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6507 | +23.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.193 | +22.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044553 | +21.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.060712 | +21.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.1953 | +20.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.028435 | +19.42 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 846 scans ; 363021 observations ; 184 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
