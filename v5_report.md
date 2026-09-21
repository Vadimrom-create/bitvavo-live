# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T14:40:12.683840+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-21T14:39:40.308829+00:00 | âge ticker : 149.8 s | durée : 150.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- STX-EUR : 0.29327 € ; score 93.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BIO-EUR : 0.025312 € ; score 88.78/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- FLUID-EUR : 1.2059 € ; score 86.18/100 ; SURVEILLE ; LOW_LIQUIDITY
- ENS-EUR : 5.8629 € ; score 85.92/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.023817 € ; score 83.86/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056362 | +72.22 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.049611 | +55.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.000972 | +41.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.102821 | +33.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.03159 | +31.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23816 | +30.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.05659 | +29.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.90956 | +26.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.052307 | +26.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROVE-EUR | 0.23942 | +24.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1083 scans ; 464095 observations ; 380 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
