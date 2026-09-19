# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T15:00:15.077109+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 34
Récupération : 2026-09-19T14:59:44.849859+00:00 | âge ticker : 158.2 s | durée : 159.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : MISSING_LATEST_CLOSED_CANDLE
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : SPREAD_RISK, INVALID_5M
- POL-EUR : STABILITY_HOLD, INVALID_5M
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- USELESS-EUR : 0.240878 € | IGNITION | score 88.23/100 | entrée 6.90/10
  Entrée 0.240741 € ; stop 0.23047 € ; TP1 0.261283 € ; TP2 0.271554 € ; montant 242.35 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.886/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.37968 € ; score 86.07/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 235.57 € ; score 84.73/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.827 € ; score 84.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 50.317 € ; score 80.61/100 ; SURVEILLE ; seuil achat non atteint
- LPT-EUR : 1.413 € ; score 79.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.071871 | +44.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.32672 | +37.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.209514 | +35.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.022314 | +25.76 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.038661 | +25.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.39293 | +24.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.081988 | +22.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0035873 | +22.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EDGE-EUR | 0.071455 | +21.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17376 | +20.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 898 scans ; 385225 observations ; 204 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
