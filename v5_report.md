# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T17:03:40.584811+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 38
Récupération : 2026-09-20T17:03:12.454541+00:00 | âge ticker : 147.8 s | durée : 148.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 41/426 ; 15 min 81/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- APT-EUR : STABILITY_HOLD, INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, INVALID_5M
- KAS-EUR : INVALID_5M
- LTC-EUR : WICK_SETUP, INVALID_5M
- NPC-EUR : INVALID_5M
- PENDLE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- POL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- QNT-EUR : INVALID_15M, INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INVALID_15M, INVALID_5M
- WAL-EUR : WICK_SETUP, INVALID_5M
- ONDO-EUR : 0.37393 € | IGNITION | score 80.37/100 | entrée 7.85/10
  Entrée 0.3738 € ; stop 0.35469 € ; TP1 0.41202 € ; TP2 0.43113 € ; montant 207.09 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.89/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.20164 € | IGNITION | score 78.21/100 | entrée 7.25/10
  Entrée 0.20174 € ; stop 0.19197 € ; TP1 0.22128 € ; TP2 0.23105 € ; montant 217.16 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.968/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 96.043 € ; score 83.43/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 81.009 € ; score 82.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : 6.8927 € ; score 77.77/100 ; SURVEILLE ; STABILITY_HOLD
- FET-EUR : 0.15615 € ; score 77.58/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.17214 € ; score 76.21/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0031335 | +46.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.029567 | +33.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.5017 | +27.83 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007626 | +25.80 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.22201 | +20.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.7108 | +18.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.049278 | +17.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.7911 | +16.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.032402 | +13.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.027209 | +12.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 997 scans ; 427459 observations ; 234 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
