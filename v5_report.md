# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T06:30:30.746742+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T06:29:59.397708+00:00 | âge ticker : 146.4 s | durée : 147.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- THE-EUR : 0.07271 € ; score 90.67/100 ; SURVEILLE ; WICK_SETUP
- KITE-EUR : 0.10907 € ; score 85.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZORA-EUR : 0.007437 € ; score 85.41/100 ; SURVEILLE ; WICK_SETUP
- MERL-EUR : 0.025051 € ; score 83.56/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 101.657 € ; score 81.65/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016389 | +110.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017443 | +107.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.124111 | +54.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.055546 | +29.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.4259e-06 | +25.58 % | DETECTED_EARLY | NONE | NONE |
| SAGA-EUR | 0.037879 | +23.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WIF-EUR | 0.21388 | +20.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27196 | +19.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.3786 | +19.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BONK-EUR | 3.1464e-06 | +18.54 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1156 scans ; 495193 observations ; 463 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
