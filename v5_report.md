# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T13:20:50.339163+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T13:20:20.368282+00:00 | âge ticker : 153.1 s | durée : 154.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- OP-EUR : 0.1245 € ; score 93.12/100 ; SURVEILLE ; STABILITY_HOLD
- ROSE-EUR : 0.007689 € ; score 93.08/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- EGLD-EUR : 4 € ; score 91.71/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7376 € ; score 89.97/100 ; SURVEILLE ; seuil achat non atteint
- CFG-EUR : 0.145893 € ; score 88.00/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 1.09878 | +51.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 138.596 | +50.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008591 | +45.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.018 | +41.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.24465 | +28.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.12587 | +23.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.54316 | +19.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006245 | +17.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.0064 | +17.17 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WLD-EUR | 0.4996 | +16.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1618 scans ; 692254 observations ; 1142 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
