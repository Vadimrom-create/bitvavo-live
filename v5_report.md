# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T02:37:59.582617+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T02:37:28.966122+00:00 | âge ticker : 153.8 s | durée : 154.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- COMP-EUR : 20.659 € ; score 93.57/100 ; SURVEILLE ; seuil achat non atteint
- BONK-EUR : 3.2668e-06 € ; score 91.86/100 ; SURVEILLE ; STABILITY_HOLD
- BOB-EUR : 0.00447 € ; score 87.98/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK, WICK_SETUP
- ICNT-EUR : 0.08972 € ; score 86.65/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.060981 € ; score 84.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ONDO-EUR | 0.47087 | +29.23 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.63165 | +28.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 78.582 | +26.55 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098984 | +25.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.037956 | +22.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.048455 | +20.64 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.16591 | +18.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22576 | +14.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19672 | +14.31 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0080493 | +14.16 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1410 scans ; 603438 observations ; 795 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
