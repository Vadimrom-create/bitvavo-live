# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T02:03:42.799342+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T02:03:10.724012+00:00 | âge ticker : 145.3 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VET-EUR : 0.0083 € ; score 90.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- IOST-EUR : 0.0008414 € ; score 86.90/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- MORPHO-EUR : 2.29967 € ; score 84.00/100 ; SURVEILLE ; seuil achat non atteint
- PARTI-EUR : 0.022614 € ; score 83.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- HBAR-EUR : 0.087264 € ; score 83.55/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BCH-EUR | 298.65 | +29.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.078116 | +24.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.51899 | +23.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.29912 | +21.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29172 | +19.95 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| DRIFT-EUR | 0.018218 | +19.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2155 | +19.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.074171 | +18.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MLN-EUR | 1.4393 | +18.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.266563 | +16.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1234 scans ; 528421 observations ; 567 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
