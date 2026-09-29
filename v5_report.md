# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T02:03:39.529475+00:00
État : OK | marchés EUR : 428 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T02:03:02.657954+00:00 | âge ticker : 156.5 s | durée : 157.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZAMA-EUR : 0.069211 € ; score 85.72/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- COW-EUR : 0.13658 € ; score 84.95/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 264.77 € ; score 83.71/100 ; SURVEILLE ; seuil achat non atteint
- CVX-EUR : 1.9344 € ; score 81.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LINK-EUR : 13.3859 € ; score 81.62/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.6067 | +42.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105763 | +24.94 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.119046 | +13.85 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.051 | +12.01 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CRV-EUR | 0.33233 | +10.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0019582 | +9.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IKA-EUR | 0.001813 | +8.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| 0G-EUR | 0.25245 | +8.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.67885 | +8.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LINK-EUR | 13.3859 | +8.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1737 scans ; 743109 observations ; 1272 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
