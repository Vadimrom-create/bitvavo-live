# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T05:49:30.811894+00:00
État : OK | marchés EUR : 426 | V4 : 375 | données valides : 426
Récupération : 2026-09-21T05:48:57.573743+00:00 | âge ticker : 147.0 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- COW-EUR : 0.13449 € ; score 92.55/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.38797 € ; score 89.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034759 € ; score 89.18/100 ; SURVEILLE ; WICK_SETUP
- CTSI-EUR : 0.025239 € ; score 89.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KSM-EUR : 3.965 € ; score 89.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.051963 | +54.50 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009109 | +46.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.25894 | +41.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057809 | +32.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.030683 | +27.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029871 | +25.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7679 | +24.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.50059 | +20.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.043953 | +20.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.050146 | +20.30 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1051 scans ; 450463 observations ; 328 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
