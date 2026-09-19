# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T13:17:40.565194+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 37
Récupération : 2026-09-19T13:17:09.700638+00:00 | âge ticker : 152.1 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 39/427 ; 15 min 83/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : INVALID_5M
- WIF-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- XLM-EUR : 0.17566 € | IGNITION | score 86.33/100 | entrée 7.60/10
  Entrée 0.17571 € ; stop 0.16758 € ; TP1 0.19197 € ; TP2 0.2001 € ; montant 225.96 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 5.881/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.36542 € ; score 82.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.337 € ; score 78.74/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.24064 € ; score 77.66/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 3.3293e-06 € ; score 76.20/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- TAO-EUR : 230.9 € ; score 75.83/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.219001 | +41.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.068367 | +41.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.023017 | +30.99 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.038887 | +30.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.147217 | +29.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.075623 | +28.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0036935 | +26.92 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29657 | +24.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0597458 | +23.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17453 | +22.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 891 scans ; 382236 observations ; 197 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
