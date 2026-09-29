# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T02:41:03.533395+00:00
État : OK | marchés EUR : 428 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T02:40:26.788221+00:00 | âge ticker : 152.2 s | durée : 153.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FIL-EUR : 0.8986 € ; score 85.05/100 ; SURVEILLE ; STABILITY_HOLD
- T-EUR : 0.00459 € ; score 83.44/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- LTC-EUR : 59.319 € ; score 81.53/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 13.2468 € ; score 80.09/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- XDC-EUR : 0.030123 € ; score 79.09/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.383 | +36.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.10447 | +24.84 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.116879 | +12.89 % | DETECTED_EARLY | NONE | NONE |
| CRV-EUR | 0.32701 | +9.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.001813 | +8.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.2468 | +7.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0019223 | +7.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.24282 | +7.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.21699 | +6.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.02383 | +6.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1739 scans ; 743965 observations ; 1273 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
