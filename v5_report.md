# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T16:47:47.753129+00:00
État : OK | marchés EUR : 428 | V4 : 403 | données valides : 427
Récupération : 2026-09-28T16:47:15.592447+00:00 | âge ticker : 151.7 s | durée : 152.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MIOTA-EUR : 0.048092 € ; score 87.29/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- EGLD-EUR : 3.9708 € ; score 86.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- ANKR-EUR : 0.0044009 € ; score 86.16/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- LINK-EUR : 13.1707 € ; score 85.95/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.070511 € ; score 84.57/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.111926 | +36.29 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 205.877 | +25.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.00197 | +19.18 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NMR-EUR | 9.9329 | +15.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.118019 | +15.00 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.025782 | +11.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.017619 | +9.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048092 | +9.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRT-EUR | 0.027413 | +8.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0046805 | +8.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1706 scans ; 729841 observations ; 1257 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
