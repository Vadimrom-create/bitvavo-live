# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T10:30:08.309414+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 31
Récupération : 2026-09-19T10:29:40.384097+00:00 | âge ticker : 145.1 s | durée : 146.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 32/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- ALGO-EUR : INVALID_5M
- APT-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_5M
- BCH-EUR : WICK_SETUP, INVALID_5M
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INVALID_5M
- KAS-EUR : INVALID_5M
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M
- VET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- WIF-EUR : INVALID_15M, INVALID_5M
- TAO-EUR : 233.39 € | IGNITION | score 88.48/100 | entrée 7.65/10
  Entrée 233.47 € ; stop 221.82 € ; TP1 256.77 € ; TP2 268.42 € ; montant 211.55 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 6.318/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.9277 € ; score 90.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0125978 € ; score 84.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- DOGE-EUR : 0.076236 € ; score 83.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.73395 € ; score 81.81/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.202 € ; score 80.90/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.21475 | +40.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EDGE-EUR | 0.07856 | +36.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.065878 | +32.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.147388 | +29.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036967 | +28.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.023954 | +28.34 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| XTZ-EUR | 0.2918 | +25.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.037382 | +25.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046774 | +23.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.38364 | +21.10 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 881 scans ; 377966 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
