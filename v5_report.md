# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T16:50:13.594690+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 36
Récupération : 2026-09-20T16:49:42.584564+00:00 | âge ticker : 155.7 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 39/426 ; 15 min 79/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- AIOZ-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- APT-EUR : INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INVALID_5M
- LTC-EUR : WICK_SETUP, INVALID_5M
- PENDLE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- POL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- TAO-EUR : BELOW_EXCHANGE_MINIMUM
- VET-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- ONDO-EUR : 0.37249 € | IGNITION | score 88.31/100 | entrée 7.30/10
  Entrée 0.3735 € ; stop 0.35434 € ; TP1 0.41182 € ; TP2 0.43098 € ; montant 206.47 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 6.134/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.20173 € | IGNITION | score 87.90/100 | entrée 7.25/10
  Entrée 0.20213 € ; stop 0.19183 € ; TP1 0.22273 € ; TP2 0.23303 € ; montant 207.69 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.737/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 95.942 € ; score 91.68/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 81.225 € ; score 83.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 228.22 € ; score 82.97/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- VET-EUR : 0.0074366 € ; score 82.30/100 ; SURVEILLE ; WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- ENA-EUR : 0.18991 € ; score 80.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0032056 | +48.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.053206 | +26.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007548 | +24.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49283 | +23.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.026671 | +21.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.22119 | +21.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.6671 | +17.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.7271 | +16.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027073 | +11.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.0315 | +11.41 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 996 scans ; 427033 observations ; 234 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
