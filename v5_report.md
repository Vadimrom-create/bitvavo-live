# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T13:54:53.093514+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 35
Récupération : 2026-09-20T13:53:50.356651+00:00 | âge ticker : 182.7 s | durée : 183.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 38/426 ; 15 min 80/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, INVALID_5M
- TRX-EUR : INVALID_15M, INVALID_5M
- HBAR-EUR : 0.074559 € | IGNITION | score 86.22/100 | entrée 7.00/10
  Entrée 0.074682 € ; stop 0.070124 € ; TP1 0.083797 € ; TP2 0.088355 € ; montant 176.94 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 5.866/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ALGO-EUR : 0.091551 € ; score 77.29/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 3.1967 € ; score 74.29/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.027086 € ; score 73.84/100 ; SURVEILLE ; seuil achat non atteint
- SAGA-EUR : 0.024452 € ; score 73.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HYPE-EUR : 79.21 € ; score 72.96/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0035621 | +71.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.46052 | +20.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.2751 | +14.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZAMA-EUR | 0.079753 | +13.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.068182 | +12.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.02533 | +10.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.041381 | +10.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.000657 | +8.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.024452 | +8.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SHELL-EUR | 0.021456 | +7.93 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 985 scans ; 422347 observations ; 229 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
