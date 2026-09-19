# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T12:57:09.646894+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 38
Récupération : 2026-09-19T12:56:39.181576+00:00 | âge ticker : 145.7 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 39/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_15M, INVALID_5M
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.4118 € | IGNITION | score 90.97/100 | entrée 7.95/10
  Entrée 1.4127 € ; stop 1.361 € ; TP1 1.5161 € ; TP2 1.5678 € ; montant 250.00 € ; risque théorique 10.87 € ; R/R net 1.52.
  Chase risk : 4.2/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.37144 € | IGNITION | score 90.74/100 | entrée 7.75/10
  Entrée 0.37162 € ; stop 0.35065 € ; TP1 0.41356 € ; TP2 0.43452 € ; montant 189.78 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 6.214/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XLM-EUR : 0.17252 € ; score 88.93/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.60946 € ; score 81.77/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80.399 € ; score 80.09/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.24115 € ; score 79.65/100 ; SURVEILLE ; WICK_SETUP
- PEPE-EUR : 3.3286e-06 € ; score 77.07/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.068071 | +43.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.04119 | +40.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.213431 | +37.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EDGE-EUR | 0.078658 | +35.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0640214 | +34.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.023237 | +30.58 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| HEI-EUR | 0.146437 | +29.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036386 | +25.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29564 | +24.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.38149 | +21.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 890 scans ; 381809 observations ; 197 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
