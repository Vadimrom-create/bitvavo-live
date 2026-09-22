# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T11:46:33.314883+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T11:46:00.110118+00:00 | âge ticker : 155.0 s | durée : 155.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- NEAR-EUR : 3.9385 € ; score 86.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.0199 € ; score 85.28/100 ; SURVEILLE ; seuil achat non atteint
- ALIGN-EUR : 0.005991 € ; score 84.50/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- COW-EUR : 0.13963 € ; score 81.37/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 83.42 € ; score 81.09/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017469 | +100.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014341 | +82.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.115898 | +34.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056288 | +32.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BTT-EUR | 3.9196e-07 | +31.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.38963 | +19.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27955 | +19.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.067795 | +18.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.22286 | +17.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3287e-06 | +17.09 % | DETECTED_EARLY | NONE | NONE |

Historique : 1179 scans ; 504991 observations ; 482 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
