# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T17:21:04.436584+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 40
Récupération : 2026-09-20T17:20:35.252129+00:00 | âge ticker : 149.6 s | durée : 150.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 45/426 ; 15 min 82/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INVALID_15M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- NPC-EUR : INVALID_5M
- PHA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- WAL-EUR : WICK_SETUP, INVALID_5M
- XPL-EUR : INVALID_5M
- ADA-EUR : 0.19993 € | IGNITION | score 85.07/100 | entrée 7.40/10
  Entrée 0.19993 € ; stop 0.19287 € ; TP1 0.21404 € ; TP2 0.2211 € ; montant 250.00 € ; risque théorique 10.55 € ; R/R net 1.50.
  Chase risk : 4.416/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LTC-EUR : 51.351 € | IGNITION | score 80.44/100 | entrée 7.40/10
  Entrée 51.381 € ; stop 49.57 € ; TP1 55.003 € ; TP2 56.814 € ; montant 250.00 € ; risque théorique 10.53 € ; R/R net 1.50.
  Chase risk : 4.605/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 95.75 € ; score 85.48/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 81.026 € ; score 80.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 228.32 € ; score 79.25/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.15548 € ; score 76.23/100 ; SURVEILLE ; seuil achat non atteint
- RAY-EUR : 1.45806 € ; score 75.37/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0032497 | +53.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.030574 | +38.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23213 | +26.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007893 | +25.52 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LUNA2-EUR | 0.050208 | +19.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.48675 | +18.40 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.073729 | +16.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.027994 | +15.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6001 | +14.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.6961 | +14.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 998 scans ; 427885 observations ; 235 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
