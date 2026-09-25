# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T02:53:53.538749+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-25T02:52:53.414506+00:00 | âge ticker : 174.3 s | durée : 175.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.081169 € ; score 90.52/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.8568 € ; score 87.75/100 ; SURVEILLE ; seuil achat non atteint
- STX-EUR : 0.27123 € ; score 87.59/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 61.972 € ; score 84.43/100 ; SURVEILLE ; WICK_SETUP
- ALICE-EUR : 0.1291 € ; score 83.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.63 | +28.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 78.969 | +26.33 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.46283 | +25.51 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098237 | +23.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.037675 | +18.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16741 | +17.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19561 | +13.93 % | DETECTED_EARLY | NONE | NONE |
| TAI-EUR | 0.004046 | +13.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021045 | +12.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.083615 | +12.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1411 scans ; 603865 observations ; 796 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
