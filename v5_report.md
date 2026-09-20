# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T16:36:04.478694+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 34
Récupération : 2026-09-20T16:35:38.280601+00:00 | âge ticker : 150.2 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 37/426 ; 15 min 77/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- AIOZ-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- APT-EUR : INVALID_5M
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INVALID_5M
- PENDLE-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- POL-EUR : WICK_SETUP, INVALID_5M
- PYTH-EUR : STABILITY_HOLD, INVALID_5M
- QNT-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : PORTFOLIO_LIMIT
- ADA-EUR : 0.19847 € | IGNITION | score 87.90/100 | entrée 7.45/10
  Entrée 0.1986 € ; stop 0.19141 € ; TP1 0.21298 € ; TP2 0.22017 € ; montant 250.00 € ; risque théorique 10.77 € ; R/R net 1.51.
  Chase risk : 3.304/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAO-EUR : 228.07 € | IGNITION | score 84.24/100 | entrée 7.40/10
  Entrée 228.38 € ; stop 217.73 € ; TP1 249.68 € ; TP2 260.33 € ; montant 224.43 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.808/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.3701 € | IGNITION | score 83.10/100 | entrée 7.05/10
  Entrée 0.37123 € ; stop 0.35397 € ; TP1 0.40575 € ; TP2 0.42301 € ; montant 23.08 € ; risque théorique 1.23 € ; R/R net 1.61.
  Chase risk : 4.26/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 95.776 € ; score 91.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0073092 € ; score 85.45/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.07555 € ; score 84.30/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.75562 € ; score 82.51/100 ; SURVEILLE ; PORTFOLIO_LIMIT
- FET-EUR : 0.15473 € ; score 82.09/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0031057 | +43.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.054496 | +30.30 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FTT-EUR | 0.23227 | +28.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49111 | +24.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007544 | +24.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.026183 | +20.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6877 | +17.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.7505 | +16.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.09743 | +10.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANTA-EUR | 0.061325 | +9.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 995 scans ; 426607 observations ; 234 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
