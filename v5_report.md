# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T17:38:42.491565+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 41
Récupération : 2026-09-20T17:38:11.283801+00:00 | âge ticker : 150.5 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 47/426 ; 15 min 82/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : SPREAD_RISK, STABILITY_HOLD, INVALID_15M, INVALID_5M
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : STABILITY_HOLD, INVALID_5M
- SHIB-EUR : STABILITY_HOLD, INVALID_5M
- WAL-EUR : STABILITY_HOLD, INVALID_5M
- XPL-EUR : 0.078787 € | IGNITION | score 81.46/100 | entrée 6.55/10
  Entrée 0.078914 € ; stop 0.07515 € ; TP1 0.086442 € ; TP2 0.090206 € ; montant 220.06 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 3.608/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.36879 € ; score 80.25/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 6.8685 € ; score 77.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HYPE-EUR : 80.769 € ; score 76.94/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 51.137 € ; score 75.04/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- AKT-EUR : 0.48772 € ; score 74.01/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0031686 | +50.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.032279 | +46.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008727 | +40.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23503 | +27.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.071706 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.04808 | +15.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.47672 | +14.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.6196 | +14.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027564 | +14.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.6588 | +13.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1001 scans ; 429163 observations ; 236 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
