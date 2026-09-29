# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T02:22:53.366639+00:00
État : OK | marchés EUR : 428 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T02:22:22.281042+00:00 | âge ticker : 144.5 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SKY-EUR : 0.068169 € ; score 85.33/100 ; SURVEILLE ; seuil achat non atteint
- MOVR-EUR : 0.8281 € ; score 84.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CRV-EUR : 0.33072 € ; score 82.39/100 ; SURVEILLE ; WICK_SETUP
- TNSR-EUR : 0.03333 € ; score 82.17/100 ; SURVEILLE ; SPREAD_RISK
- COW-EUR : 0.13658 € ; score 82.06/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.6081 | +39.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105064 | +24.37 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.119571 | +14.66 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.050754 | +11.97 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| 0G-EUR | 0.24986 | +10.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.33072 | +9.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.001813 | +8.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.3471 | +8.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0019262 | +7.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.22094 | +7.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1738 scans ; 743537 observations ; 1273 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
