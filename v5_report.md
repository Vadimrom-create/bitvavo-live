# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T12:42:48.644995+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 36
Récupération : 2026-09-19T12:42:21.099320+00:00 | âge ticker : 144.4 s | durée : 145.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 37/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- QNT-EUR : INVALID_5M
- RENDER-EUR : INVALID_5M
- W-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- ONDO-EUR : 0.3675 € | IGNITION | score 83.35/100 | entrée 7.95/10
  Entrée 0.3675 € ; stop 0.35089 € ; TP1 0.40072 € ; TP2 0.41733 € ; montant 230.60 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.538/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XLM-EUR : 0.17032 € ; score 83.20/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.575 € ; score 82.63/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COTI-EUR : 0.018347 € ; score 78.29/100 ; SURVEILLE ; WICK_SETUP
- RAY-EUR : 1.57522 € ; score 76.93/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- FET-EUR : 0.15917 € ; score 76.84/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.081566 | +40.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.040796 | +39.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.211307 | +36.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.065987 | +35.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.14819 | +31.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.023101 | +29.39 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| CAP-EUR | 0.0605933 | +27.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036725 | +26.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.38962 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17288 | +21.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 889 scans ; 381382 observations ; 197 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
