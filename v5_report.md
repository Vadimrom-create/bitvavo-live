# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T14:43:56.153557+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 31
Récupération : 2026-09-20T14:43:24.203042+00:00 | âge ticker : 150.2 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/426 ; 15 min 76/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : INVALID_15M, INVALID_5M
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.075275 € ; score 82.58/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.7177 € ; score 81.86/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.027078 € ; score 80.38/100 ; SURVEILLE ; WICK_SETUP
- ALGO-EUR : 0.093827 € ; score 79.50/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.19308 € ; score 75.14/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0037508 | +80.47 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49129 | +28.79 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007142 | +18.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.073783 | +17.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.4674 | +16.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CTSI-EUR | 0.025599 | +11.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.030622 | +9.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.076546 | +7.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.024385 | +7.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.093827 | +6.75 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 988 scans ; 423625 observations ; 230 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
