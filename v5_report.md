# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T03:37:39.542260+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T03:37:07.045309+00:00 | âge ticker : 159.5 s | durée : 161.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CAKE-EUR : 2.4819 € ; score 94.21/100 ; SURVEILLE ; WICK_SETUP
- ZAMA-EUR : 0.079115 € ; score 90.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- AVNT-EUR : 0.10989 € ; score 89.03/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.3237 € ; score 87.36/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.103473 € ; score 85.87/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.074015 | +69.78 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0012931 | +66.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24196 | +42.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.037675 | +38.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.7815 | +27.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.105 | +22.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.73937 | +20.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.23588 | +20.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013384 | +18.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.063992 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1499 scans ; 641441 observations ; 941 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
