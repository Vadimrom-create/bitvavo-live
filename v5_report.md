# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T08:39:39.451463+00:00
État : OK | marchés EUR : 426 | V4 : 350 | données valides : 426
Récupération : 2026-10-04T08:38:35.885869+00:00 | âge ticker : 177.5 s | durée : 179.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 162.2 € ; score 85.23/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FLUID-EUR : 1.528 € ; score 77.74/100 ; SURVEILLE ; WICK_SETUP
- SKY-EUR : 0.085314 € ; score 77.74/100 ; SURVEILLE ; seuil achat non atteint
- MAGIC-EUR : 0.052725 € ; score 77.24/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CHZ-EUR : 0.015372 € ; score 76.79/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BEAM-EUR | 0.0025805 | +37.57 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.010917 | +34.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.115344 | +27.65 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TREAD-EUR | 1.01475 | +26.83 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.048315 | +25.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUN-EUR | 0.018708 | +20.81 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ATH-EUR | 0.0069949 | +16.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AKT-EUR | 0.66678 | +16.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PUMP-EUR | 0.0056756 | +15.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZAMA-EUR | 0.079524 | +14.14 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2051 scans ; 877712 observations ; 1628 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
