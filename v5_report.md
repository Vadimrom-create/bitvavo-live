# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T01:05:22.899489+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-30T01:04:47.230913+00:00 | âge ticker : 151.7 s | durée : 152.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- XDC-EUR : 0.02943 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP
- BIO-EUR : 0.027694 € ; score 85.51/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZETA-EUR : 0.045759 € ; score 84.93/100 ; SURVEILLE ; seuil achat non atteint
- SYN-EUR : 0.147618 € ; score 84.24/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.008 € ; score 81.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.37842 | +47.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016543 | +31.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.0924 | +31.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.65415 | +26.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 240.987 | +22.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051573 | +18.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRIA-EUR | 0.004066 | +16.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.089675 | +15.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022453 | +15.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.5553 | +14.99 % | DETECTED_EARLY | NONE | NONE |

Historique : 1806 scans ; 772684 observations ; 1349 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
