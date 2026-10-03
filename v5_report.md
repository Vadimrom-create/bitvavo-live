# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T11:12:53.199917+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-10-03T11:12:20.869446+00:00 | âge ticker : 154.9 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 161.67 € ; score 86.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.8113e-06 € ; score 85.23/100 ; SURVEILLE ; WICK_SETUP
- STRK-EUR : 0.0392 € ; score 84.65/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.22257 € ; score 84.38/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.030983 € ; score 83.50/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GLMR-EUR | 0.010241 | +33.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006445 | +14.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ATH-EUR | 0.0063405 | +13.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.065198 | +12.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.064066 | +11.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.53206 | +11.41 % | DETECTED_EARLY | NONE | NONE |
| SUPER-EUR | 0.21884 | +9.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 229.885 | +8.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006317 | +8.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.65568 | +7.45 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2045 scans ; 875156 observations ; 1610 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
