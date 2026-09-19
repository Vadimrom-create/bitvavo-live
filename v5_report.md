# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T16:36:42.003697+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 31
Récupération : 2026-09-19T16:35:38.807750+00:00 | âge ticker : 186.1 s | durée : 187.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/427 ; 15 min 86/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INVALID_5M
- SENT-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- WAL-EUR : WICK_SETUP, INVALID_5M
- PEPE-EUR : 3.4142e-06 € | IGNITION | score 93.41/100 | entrée 7.95/10
  Entrée 3.4162e-06 € ; stop 3.2917e-06 € ; TP1 3.6651e-06 € ; TP2 3.7896e-06 € ; montant 250.00 € ; risque théorique 10.83 € ; R/R net 1.51.
  Chase risk : 3.613/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ETH-EUR : 2305.97 € ; score 82.31/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.936 € ; score 80.31/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 236.52 € ; score 79.11/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 97.226 € ; score 76.73/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.37594 € ; score 74.71/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.074722 | +42.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.009969 | +31.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31832 | +31.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.207403 | +30.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.3956 | +24.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.072998 | +24.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.1786 | +23.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.079668 | +20.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.021679 | +20.21 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AVAX-EUR | 8.4122 | +19.07 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 904 scans ; 387787 observations ; 210 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
