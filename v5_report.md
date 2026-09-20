# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T14:56:48.743336+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 34
Récupération : 2026-09-20T14:56:21.827749+00:00 | âge ticker : 142.0 s | durée : 142.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/426 ; 15 min 73/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : INVALID_15M, INVALID_5M

## SURVEILLE

- ALGO-EUR : 0.096 € ; score 85.48/100 ; SURVEILLE ; WICK_SETUP
- HBAR-EUR : 0.076559 € ; score 82.11/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.5899 € ; score 79.07/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.027181 € ; score 78.40/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 79.32 € ; score 74.63/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0038235 | +83.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.076673 | +27.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007152 | +18.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.44954 | +16.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.4633 | +15.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CTSI-EUR | 0.025643 | +12.08 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.024796 | +11.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.096 | +9.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.030479 | +9.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.076559 | +8.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 989 scans ; 424051 observations ; 230 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
