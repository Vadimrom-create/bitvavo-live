# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T07:14:29.876068+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T07:14:05.619145+00:00 | âge ticker : 141.0 s | durée : 142.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUPER-EUR : 0.1506 € ; score 91.94/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 6.916 € ; score 91.66/100 ; SURVEILLE ; WICK_SETUP
- TAIKO-EUR : 0.07973 € ; score 91.62/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.083341 € ; score 88.70/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.030669 € ; score 88.49/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 90.384 | +43.13 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.69941 | +40.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.103948 | +31.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48101 | +27.31 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.049796 | +22.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.085656 | +18.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17668 | +18.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.038278 | +17.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021603 | +16.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AXS-EUR | 1.0623 | +15.20 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1426 scans ; 610270 observations ; 817 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
