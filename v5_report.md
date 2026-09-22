# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T17:45:58.502570+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-09-22T17:45:30.034133+00:00 | âge ticker : 152.7 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LPT-EUR : 1.5 € ; score 91.81/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 84.337 € ; score 91.68/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SOMI-EUR : 0.16624 € ; score 91.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- VIRTUAL-EUR : 0.63995 € ; score 88.06/100 ; SURVEILLE ; seuil achat non atteint
- SSV-EUR : 2.8849 € ; score 88.04/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.021557 | +43.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.071174 | +29.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 287.65 | +25.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050364 | +23.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2536 | +23.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.37989 | +19.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.11942 | +16.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.075413 | +15.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MERL-EUR | 0.027261 | +15.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.038537 | +14.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1202 scans ; 514789 observations ; 529 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
