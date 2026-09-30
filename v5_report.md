# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T05:01:25.382909+00:00
État : OK | marchés EUR : 429 | V4 : 391 | données valides : 429
Récupération : 2026-09-30T05:00:55.408179+00:00 | âge ticker : 155.5 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HUMA-EUR : 0.026445 € ; score 93.54/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 3.014 € ; score 92.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7132 € ; score 92.26/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.01881 € ; score 91.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.44257 € ; score 91.33/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36919 | +43.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.1579 | +37.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016987 | +32.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0024294 | +29.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6414 | +23.37 % | DETECTED_EARLY | NONE | NONE |
| MEW-EUR | 0.00049143 | +20.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.06403 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.005041 | +17.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 249.634 | +16.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.091179 | +16.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1818 scans ; 777832 observations ; 1355 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
