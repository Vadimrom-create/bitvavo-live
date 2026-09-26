# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T19:17:39.760008+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T19:17:06.006127+00:00 | âge ticker : 156.2 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NPC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AEVO-EUR : 0.024326 € ; score 92.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AVNT-EUR : 0.11511 € ; score 91.57/100 ; SURVEILLE ; seuil achat non atteint
- MAVIA-EUR : 0.03181 € ; score 88.87/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- NPC-EUR : 0.0206738 € ; score 87.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MANA-EUR : 0.080709 € ; score 87.02/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.001813 | +127.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006348 | +43.10 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.12372 | +38.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019878 | +35.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 107.08 | +24.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.04401 | +21.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061958 | +20.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.006065 | +18.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KAS-EUR | 0.043311 | +17.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47072 | +15.85 % | DETECTED_EARLY | NONE | NONE |

Historique : 1555 scans ; 665353 observations ; 1028 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
