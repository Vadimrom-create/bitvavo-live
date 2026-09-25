# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T17:05:20.207974+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T17:04:42.381146+00:00 | âge ticker : 157.1 s | durée : 158.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STX-EUR : 0.28568 € ; score 90.56/100 ; SURVEILLE ; WICK_SETUP
- MAVIA-EUR : 0.030001 € ; score 87.33/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- ROSE-EUR : 0.0072 € ; score 86.33/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- YGG-EUR : 0.023963 € ; score 86.13/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 134.79 € ; score 85.29/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.069033 | +56.10 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RARE-EUR | 0.014881 | +28.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.20262 | +26.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08946 | +22.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.65929 | +21.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74212 | +20.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.46061 | +19.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22931 | +19.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 86.261 | +15.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.020457 | +14.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1458 scans ; 623934 observations ; 877 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
