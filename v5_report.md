# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T20:49:16.589026+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T20:48:43.520083+00:00 | âge ticker : 157.4 s | durée : 158.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CFG-EUR : 0.143913 € ; score 93.77/100 ; SURVEILLE ; seuil achat non atteint
- APE-EUR : 0.14727 € ; score 93.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- GALA-EUR : 0.0020298 € ; score 92.69/100 ; SURVEILLE ; seuil achat non atteint
- SAFE-EUR : 0.102952 € ; score 91.58/100 ; SURVEILLE ; LOW_LIQUIDITY
- GMT-EUR : 0.007841 € ; score 88.95/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 169.399 | +59.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28472 | +46.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006629 | +30.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.92188 | +26.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013823 | +23.97 % | DETECTED_EARLY | NONE | NONE |
| GRT-EUR | 0.028461 | +18.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0044175 | +16.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0011606 | +15.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007216 | +15.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NEAR-EUR | 4.7991 | +14.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1645 scans ; 703783 observations ; 1171 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
