# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T22:57:09.405582+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T22:56:40.586471+00:00 | âge ticker : 155.2 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- A-EUR : 0.086497 € ; score 91.42/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- DOT-EUR : 1.063 € ; score 91.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.8099 € ; score 90.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ROSE-EUR : 0.007072 € ; score 89.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MON-EUR : 0.023406 € ; score 89.35/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020436 | +36.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.055193 | +31.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.304049 | +27.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 296.15 | +25.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019389 | +24.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FLOCK-EUR | 0.07843 | +22.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2179 | +17.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12206 | +17.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GOAT-EUR | 0.018404 | +15.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UNI-EUR | 8.9657 | +14.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1223 scans ; 523735 observations ; 553 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
