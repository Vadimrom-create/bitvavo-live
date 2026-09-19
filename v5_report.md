# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T17:59:33.447071+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 34
Récupération : 2026-09-19T17:59:01.203936+00:00 | âge ticker : 158.6 s | durée : 160.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 37/427 ; 15 min 94/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : INVALID_5M
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- PEPE-EUR : 3.6143e-06 € | IGNITION | score 82.34/100 | entrée 6.90/10
  Entrée 3.6257e-06 € ; stop 3.3096e-06 € ; TP1 4.2578e-06 € ; TP2 4.5739e-06 € ; montant 127.83 € ; risque théorique 12.00 € ; R/R net 1.78.
  Chase risk : 8.873/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SUI-EUR : 0.74861 € ; score 91.00/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034835 € ; score 84.55/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.245 € ; score 79.54/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 96.956 € ; score 75.08/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- TAO-EUR : 230.19 € ; score 74.93/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.072307 | +39.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.209762 | +36.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.41984 | +32.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31604 | +29.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.9755 | +26.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.073205 | +25.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17454 | +21.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.3885 | +18.42 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CROSS-EUR | 0.135512 | +16.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALLO-EUR | 0.212891 | +16.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 911 scans ; 390776 observations ; 212 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
