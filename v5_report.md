# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T09:42:20.730842+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 30
Récupération : 2026-09-19T09:41:51.590797+00:00 | âge ticker : 162.4 s | durée : 163.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 34/427 ; 15 min 75/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- KAS-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- TAO-EUR : 231.27 € | IGNITION | score 90.53/100 | entrée 7.40/10
  Entrée 231.19 € ; stop 218.04 € ; TP1 257.49 € ; TP2 270.64 € ; montant 188.44 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 4.11/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.61177 € | IGNITION | score 81.08/100 | entrée 8.20/10
  Entrée 1.61448 € ; stop 1.53556 € ; TP1 1.77231 € ; TP2 1.85123 € ; montant 215.40 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.534/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.35137 € ; score 91.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.28 € ; score 80.46/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.15832 € ; score 78.06/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.8212 € ; score 74.99/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SOL-EUR : 97.159 € ; score 74.96/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.225057 | +46.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.065675 | +34.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.077001 | +33.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.14626 | +28.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036849 | +27.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29853 | +27.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.047092 | +25.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.023239 | +24.03 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| EPIC-EUR | 0.37671 | +19.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MORPHO-EUR | 2.41946 | +19.13 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 878 scans ; 376685 observations ; 191 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
