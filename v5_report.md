# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T03:28:29.887329+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T03:27:54.206266+00:00 | âge ticker : 146.2 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.19384 € ; score 87.72/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.029811 € ; score 85.67/100 ; SURVEILLE ; seuil achat non atteint
- BNB-EUR : 678.82 € ; score 85.33/100 ; SURVEILLE ; seuil achat non atteint
- ACU-EUR : 0.10942 € ; score 83.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- LTC-EUR : 62.561 € ; score 82.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 80.346 | +29.34 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098761 | +24.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45519 | +24.43 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.59715 | +23.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.038067 | +18.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16926 | +18.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.084124 | +16.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FET-EUR | 0.19702 | +14.94 % | DETECTED_EARLY | NONE | NONE |
| DEEP-EUR | 0.018605 | +12.98 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SNX-EUR | 0.22934 | +12.11 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1413 scans ; 604719 observations ; 797 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
