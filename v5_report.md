# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T01:08:59.016580+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 23
Récupération : 2026-09-19T01:08:27.439985+00:00 | âge ticker : 150.3 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/427 ; 15 min 65/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- AVAX-EUR : INVALID_5M
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- PYTH-EUR : INVALID_15M, INVALID_5M
- W-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- HYPE-EUR : 81.394 € ; score 91.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.34977 € ; score 85.71/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : 70792 € ; score 83.80/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.16026 € ; score 76.81/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.22193 € ; score 71.66/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.0044843 | +60.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0063422 | +50.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037666 | +48.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.199829 | +24.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.05403 | +24.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044489 | +21.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6416 | +21.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028475 | +19.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2871 | +19.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.061815 | +19.23 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 847 scans ; 363448 observations ; 185 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
