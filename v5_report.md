# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T01:13:25.285201+00:00
État : OK | marchés EUR : 428 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T01:12:54.321357+00:00 | âge ticker : 150.0 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HUMA-EUR : 0.0248 € ; score 92.29/100 ; SURVEILLE ; seuil achat non atteint
- DIA-EUR : 0.14041 € ; score 88.61/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- CFG-EUR : 0.13649 € ; score 87.37/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.030622 € ; score 84.34/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : 2347.9 € ; score 83.50/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.7339 | +29.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105385 | +23.70 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.118343 | +12.77 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.25494 | +11.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.001813 | +8.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.4454 | +8.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.2072 | +8.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0493875 | +8.25 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZBCN-EUR | 0.0019502 | +8.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CRV-EUR | 0.3269 | +7.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1734 scans ; 741825 observations ; 1272 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
