# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T22:10:48.895529+00:00
État : OK | marchés EUR : 426 | V4 : 395 | données valides : 426
Récupération : 2026-09-22T22:10:18.913933+00:00 | âge ticker : 155.2 s | durée : 156.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SAFE-EUR : 0.097952 € ; score 90.31/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- ANIME-EUR : 0.0030624 € ; score 89.65/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- ETHFI-EUR : 0.60591 € ; score 85.22/100 ; SURVEILLE ; seuil achat non atteint
- NEO-EUR : 2.2911 € ; score 83.59/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.0606 € ; score 82.72/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| KERNEL-EUR | 0.056694 | +35.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.019141 | +30.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01945 | +25.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.307183 | +24.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 293.18 | +24.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.076578 | +19.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.1211 | +16.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.068467 | +14.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.1809 | +14.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GOAT-EUR | 0.018162 | +13.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1220 scans ; 522457 observations ; 545 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
