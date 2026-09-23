# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T02:23:47.315932+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T02:23:14.887411+00:00 | âge ticker : 146.3 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AERO-EUR : 0.63164 € ; score 93.14/100 ; SURVEILLE ; WICK_SETUP
- CHIP-EUR : 0.040979 € ; score 89.56/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0083056 € ; score 85.75/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAIA-EUR : 0.029295 € ; score 85.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KAT-EUR : 0.004435 € ; score 84.45/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.080638 | +32.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 297.22 | +28.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.525 | +25.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.298588 | +24.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29232 | +20.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRO-EUR | 1.2241 | +19.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018175 | +19.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.062947 | +19.07 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FLOCK-EUR | 0.073955 | +18.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MLN-EUR | 1.4384 | +18.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1235 scans ; 528847 observations ; 568 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
