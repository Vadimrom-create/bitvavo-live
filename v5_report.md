# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T23:33:56.224849+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T23:33:27.145935+00:00 | âge ticker : 151.5 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AERO-EUR : 0.61342 € ; score 92.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- 0G-EUR : 0.20376 € ; score 91.23/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AVNT-EUR : 0.10102 € ; score 88.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : 6.8758 € ; score 86.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0038011 € ; score 86.62/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0013702 | +75.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0145 | +69.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.124491 | +57.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.051127 | +48.40 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.3174 | +40.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008724 | +36.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043531 | +32.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010914 | +32.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.026571 | +26.16 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WIF-EUR | 0.21189 | +20.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1131 scans ; 484543 observations ; 411 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
