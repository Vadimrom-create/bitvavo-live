# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T03:47:04.430167+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T03:46:29.105597+00:00 | âge ticker : 159.6 s | durée : 160.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SENT-EUR : 0.018528 € ; score 88.82/100 ; SURVEILLE ; WICK_SETUP
- NPC-EUR : 0.0195001 € ; score 86.92/100 ; SURVEILLE ; seuil achat non atteint
- ANIME-EUR : 0.0029378 € ; score 86.49/100 ; SURVEILLE ; LOW_LIQUIDITY
- MET-EUR : 0.29141 € ; score 85.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- COW-EUR : 0.12563 € ; score 85.24/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 80.603 | +29.70 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.6324 | +28.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.100061 | +26.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46183 | +25.79 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038657 | +23.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.085194 | +18.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.1697 | +17.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19704 | +14.19 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0078833 | +13.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SNX-EUR | 0.231 | +12.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1414 scans ; 605146 observations ; 797 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
