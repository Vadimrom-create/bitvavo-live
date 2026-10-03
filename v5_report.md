# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T09:41:10.503378+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T09:40:10.559143+00:00 | âge ticker : 174.3 s | durée : 175.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HUMA-EUR : 0.028723 € ; score 90.77/100 ; SURVEILLE ; SPREAD_RISK
- BAT-EUR : 0.08536 € ; score 88.86/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 1.04292 € ; score 87.99/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.40131 € ; score 86.25/100 ; SURVEILLE ; seuil achat non atteint
- AKT-EUR : 0.57632 € ; score 86.07/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HFT-EUR | 0.00719 | +28.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.065786 | +16.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 234.269 | +12.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065 | +12.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.0062877 | +12.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.66556 | +8.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GLMR-EUR | 0.008507 | +7.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.2148 | +6.62 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CAP-EUR | 0.0629748 | +6.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.096255 | +5.47 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2041 scans ; 873452 observations ; 1608 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
