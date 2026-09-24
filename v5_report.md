# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T21:47:59.934712+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T21:47:28.505308+00:00 | âge ticker : 151.9 s | durée : 153.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ADA-EUR : 0.21966 € ; score 89.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TURBO-EUR : 0.0009329 € ; score 89.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ICP-EUR : 2.7586 € ; score 88.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BNT-EUR : 0.29925 € ; score 85.02/100 ; SURVEILLE ; LOW_LIQUIDITY
- DUSK-EUR : 0.077461 € ; score 84.71/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0092256 | +33.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.03923 | +27.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.46186 | +26.90 % | DETECTED_EARLY | NONE | NONE |
| LSK-EUR | 0.38449 | +26.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.0996 | +25.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 78.243 | +25.34 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.56333 | +23.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.053713 | +22.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.16819 | +21.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHIP-EUR | 0.043847 | +18.61 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1393 scans ; 596179 observations ; 764 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
