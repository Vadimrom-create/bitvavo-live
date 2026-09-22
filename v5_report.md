# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T22:27:53.579299+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T22:27:26.934634+00:00 | âge ticker : 149.9 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SSV-EUR : 2.8612 € ; score 92.17/100 ; SURVEILLE ; WICK_SETUP
- MANA-EUR : 0.076485 € ; score 90.47/100 ; SURVEILLE ; seuil achat non atteint
- MAGIC-EUR : 0.045577 € ; score 89.58/100 ; SURVEILLE ; seuil achat non atteint
- SUSHI-EUR : 0.23032 € ; score 89.11/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.011391 € ; score 89.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| KERNEL-EUR | 0.056767 | +35.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.019577 | +32.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019581 | +26.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.305571 | +25.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 293.15 | +24.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.076552 | +19.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2037 | +16.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12092 | +16.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.06822 | +16.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NES-EUR | 0.14116 | +15.42 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1221 scans ; 522883 observations ; 548 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
