# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T07:37:45.490704+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-10-03T07:36:46.384646+00:00 | âge ticker : 173.4 s | durée : 174.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CVX-EUR : 2.0597 € ; score 86.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RAY-EUR : 1.79121 € ; score 85.36/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 160.14 € ; score 82.65/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDP-EUR : 0.017975 € ; score 82.00/100 ; SURVEILLE ; seuil achat non atteint
- IMX-EUR : 0.16726 € ; score 81.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.06764 | +32.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 234.464 | +14.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.17633 | +12.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0059956 | +12.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.063172 | +10.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.100661 | +10.58 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENJ-EUR | 0.030876 | +9.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.21325 | +9.07 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.006215 | +8.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IMX-EUR | 0.16726 | +8.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2035 scans ; 870896 observations ; 1605 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
