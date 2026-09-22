# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T06:44:32.865460+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T06:44:00.135758+00:00 | âge ticker : 155.0 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LPT-EUR : 1.4729 € ; score 91.17/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 82.258 € ; score 89.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0034024 € ; score 87.56/100 ; SURVEILLE ; seuil achat non atteint
- AIXBT-EUR : 0.020388 € ; score 86.88/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- KAT-EUR : 0.004284 € ; score 86.68/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015729 | +102.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017028 | +102.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.121742 | +50.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.4412e-06 | +26.84 % | DETECTED_EARLY | NONE | NONE |
| KERNEL-EUR | 0.055444 | +25.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.21649 | +22.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.38312 | +21.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27307 | +20.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAO-EUR | 279.49 | +19.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FARTCOIN-EUR | 0.17735 | +19.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1158 scans ; 496045 observations ; 463 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
