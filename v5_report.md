# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T09:34:57.260610+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-26T09:34:25.428751+00:00 | âge ticker : 155.1 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AXS-EUR : 1.0566 € ; score 93.76/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 276 € ; score 88.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7494 € ; score 87.23/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AEVO-EUR : 0.023223 € ; score 86.41/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- 0G-EUR : 0.23379 € ; score 85.24/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019874 | +156.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018953 | +64.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.068252 | +41.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24172 | +28.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.067771 | +26.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.2447 | +25.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.098831 | +18.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.79185 | +17.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038791 | +15.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TNSR-EUR | 0.038705 | +14.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1520 scans ; 650408 observations ; 968 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
