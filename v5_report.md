# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T00:36:49.425527+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 23
Récupération : 2026-09-19T00:36:17.531867+00:00 | âge ticker : 152.5 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 23/427 ; 15 min 68/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : EXTENDED_24H, CHASE_RISK, INVALID_5M
- KAS-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- LTC-EUR : INVALID_5M
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INVALID_5M
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ONDO-EUR : 0.35104 € ; score 88.34/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 220.99 € ; score 85.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.16157 € ; score 85.66/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.904 € ; score 80.26/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.23112 € ; score 72.59/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| F-EUR | 0.004375 | +56.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0064703 | +55.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037753 | +49.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.061226 | +23.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| APT-EUR | 0.6496 | +23.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19208 | +23.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053591 | +22.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044706 | +22.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2514 | +20.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.197066 | +20.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 845 scans ; 362594 observations ; 184 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
