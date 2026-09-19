# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T10:44:55.950952+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 33
Récupération : 2026-09-19T10:44:28.392408+00:00 | âge ticker : 146.1 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 34/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- APT-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- HBAR-EUR : WICK_SETUP, INVALID_5M
- JUP-EUR : WICK_SETUP, INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M
- VET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- WIF-EUR : INVALID_15M, INVALID_5M
- SUI-EUR : 0.74379 € | IGNITION | score 90.42/100 | entrée 8.20/10
  Entrée 0.74412 € ; stop 0.70694 € ; TP1 0.81848 € ; TP2 0.85566 € ; montant 211.30 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.414/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAO-EUR : 233.74 € | IGNITION | score 84.09/100 | entrée 7.35/10
  Entrée 233.77 € ; stop 221.82 € ; TP1 257.67 € ; TP2 269.62 € ; montant 207.11 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 6.495/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.9663 € ; score 89.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.35645 € ; score 88.68/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.07601 € ; score 85.05/100 ; SURVEILLE ; WICK_SETUP
- APT-EUR : 0.6352 € ; score 83.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.012615 € ; score 79.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.218895 | +43.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.067978 | +37.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.077991 | +35.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.024182 | +31.76 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.038938 | +31.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036828 | +28.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.145547 | +26.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.29245 | +25.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.047009 | +25.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.39396 | +24.36 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 882 scans ; 378393 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
