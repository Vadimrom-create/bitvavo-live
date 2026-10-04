# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T16:42:20.683597+00:00
État : OK | marchés EUR : 426 | V4 : 353 | données valides : 426
Récupération : 2026-10-04T16:41:14.912164+00:00 | âge ticker : 189.6 s | durée : 190.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STX-EUR : 0.35692 € ; score 84.70/100 ; SURVEILLE ; WICK_SETUP
- FLUID-EUR : 1.551 € ; score 81.91/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.082357 € ; score 81.61/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 159.3 € ; score 79.35/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.22946 € ; score 78.52/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOS-EUR | 0.67914 | +26.17 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDGE-EUR | 0.112458 | +24.54 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BEAM-EUR | 0.002308 | +23.09 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GTC-EUR | 0.123194 | +21.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AKT-EUR | 0.6969 | +16.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.049718 | +14.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.021887 | +13.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AXS-EUR | 1.2015 | +12.87 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023419 | +12.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.03191 | +12.79 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2058 scans ; 880694 observations ; 1629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
