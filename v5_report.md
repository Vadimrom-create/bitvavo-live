# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T12:24:29.476581+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T12:23:59.167044+00:00 | âge ticker : 146.3 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SKL-EUR : 0.003978 € ; score 86.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XRP-EUR : 1.34091 € ; score 84.79/100 ; SURVEILLE ; seuil achat non atteint
- QNT-EUR : 62.475 € ; score 83.74/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 102.365 € ; score 82.45/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 83.531 € ; score 81.55/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0174 | +97.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014293 | +81.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.055531 | +32.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.071497 | +25.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.117165 | +23.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28482 | +21.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.38194 | +17.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.22643 | +17.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2647e-06 | +15.64 % | DETECTED_EARLY | NONE | NONE |
| TAO-EUR | 283.15 | +14.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1182 scans ; 506269 observations ; 491 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
