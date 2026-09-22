# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T17:31:33.407208+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T17:31:04.025800+00:00 | âge ticker : 152.5 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- BEAM-EUR : 0.0016634 € ; score 91.71/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.006903 € ; score 91.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ALGO-EUR : 0.097471 € ; score 91.17/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.036474 € ; score 89.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- METIS-EUR : 3.1021 € ; score 88.09/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.022672 | +49.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.072082 | +32.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 288.31 | +25.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050521 | +24.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2387 | +21.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.38043 | +19.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.076257 | +16.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.039071 | +16.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.11891 | +15.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.110703 | +14.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1201 scans ; 514363 observations ; 529 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
