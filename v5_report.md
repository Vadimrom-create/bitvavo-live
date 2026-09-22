# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T09:09:57.777641+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T09:09:33.255144+00:00 | âge ticker : 142.4 s | durée : 143.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SHIB-EUR : 5.2913e-06 € ; score 90.19/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CRO-EUR : 0.05747 € ; score 89.64/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.21624 € ; score 89.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RSR-EUR : 0.0014556 € ; score 88.61/100 ; SURVEILLE ; WICK_SETUP
- ZRX-EUR : 0.103506 € ; score 88.47/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.019676 | +125.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014891 | +89.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.120609 | +45.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057962 | +36.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39866 | +24.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.22451 | +23.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3634e-06 | +20.92 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.46064 | +19.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| THQ-EUR | 0.011279 | +17.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CARV-EUR | 0.040278 | +17.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1170 scans ; 501157 observations ; 471 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
