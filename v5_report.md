# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T03:50:04.239106+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T03:49:32.500842+00:00 | âge ticker : 157.1 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.08156 € ; score 92.13/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.08116 € ; score 91.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.056394 € ; score 89.18/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MEME-EUR : 0.00053722 € ; score 87.80/100 ; SURVEILLE ; SPREAD_RISK
- 0G-EUR : 0.20624 € ; score 85.16/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0165 | +91.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013374 | +72.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.055785 | +48.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.048026 | +42.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.111825 | +40.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.053036 | +37.91 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PEPE-EUR | 4.5241e-06 | +29.39 % | DETECTED_EARLY | NONE | NONE |
| CARV-EUR | 0.041186 | +25.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WIF-EUR | 0.219 | +23.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.2761 | +21.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1146 scans ; 490933 observations ; 451 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
