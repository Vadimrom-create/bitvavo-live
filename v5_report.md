# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T11:12:17.141603+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T11:11:43.417913+00:00 | âge ticker : 145.9 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.09978 € ; score 89.93/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BABY-EUR : 0.011235 € ; score 83.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- COW-EUR : 0.13945 € ; score 82.65/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 5.1307e-06 € ; score 82.18/100 ; SURVEILLE ; seuil achat non atteint
- LIGHTER-EUR : 4.1326 € ; score 81.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017434 | +98.56 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.001445 | +84.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.116246 | +35.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.055136 | +25.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069199 | +23.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28481 | +22.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| U-EUR | 0.0002606 | +20.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.5 | +19.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.38848 | +19.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2982e-06 | +17.79 % | DETECTED_EARLY | NONE | NONE |

Historique : 1177 scans ; 504139 observations ; 479 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
