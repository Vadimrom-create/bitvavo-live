# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T10:59:11.171590+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-23T10:58:41.901055+00:00 | âge ticker : 150.9 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CAKE-EUR : 2.2998 € ; score 90.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- JASMY-EUR : 0.0040615 € ; score 88.88/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- KITE-EUR : 0.12005 € ; score 87.20/100 ; SURVEILLE ; seuil achat non atteint
- ZBT-EUR : 0.082114 € ; score 84.37/100 ; SURVEILLE ; seuil achat non atteint
- ZEN-EUR : 7.2173 € ; score 83.74/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034074 | +39.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.34889 | +37.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 308.08 | +30.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01966 | +30.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.2998 | +27.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16509 | +26.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.085958 | +23.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TIA-EUR | 0.46647 | +22.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.277597 | +22.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BONK-EUR | 3.559e-06 | +19.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1264 scans ; 541201 observations ; 641 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
