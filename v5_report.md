# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T10:39:33.257361+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T10:38:32.735221+00:00 | âge ticker : 189.0 s | durée : 189.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZBCN-EUR : 0.0017543 € ; score 87.09/100 ; SURVEILLE ; LOW_LIQUIDITY, WIDE_SPREAD_RISK
- GRAM-EUR : 1.2394 € ; score 85.16/100 ; SURVEILLE ; WICK_SETUP
- ZEN-EUR : 6.5927 € ; score 84.96/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BCH-EUR : 238.31 € ; score 83.38/100 ; SURVEILLE ; seuil achat non atteint
- LUNA2-EUR : 0.046362 € ; score 82.49/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017498 | +99.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015078 | +92.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.115802 | +39.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056898 | +29.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39416 | +21.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.069526 | +21.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.22228 | +20.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.0413 | +20.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.291e-06 | +18.10 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.46164 | +17.17 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1175 scans ; 503287 observations ; 479 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
