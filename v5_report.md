# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T02:41:28.890772+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-23T02:40:59.782277+00:00 | âge ticker : 144.9 s | durée : 145.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- BEAM-EUR : 0.0016919 € ; score 92.10/100 ; SURVEILLE ; SPREAD_RISK
- FLOKI-EUR : 2.6498e-05 € ; score 89.82/100 ; SURVEILLE ; seuil achat non atteint
- MAVIA-EUR : 0.029682 € ; score 89.12/100 ; SURVEILLE ; WICK_SETUP
- RARE-EUR : 0.012123 € ; score 88.93/100 ; SURVEILLE ; SPREAD_RISK
- RE-EUR : 0.41328 € ; score 86.62/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.080624 | +31.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 297.04 | +27.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.5209 | +24.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.29499 | +23.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.29421 | +21.78 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| UP-EUR | 0.064628 | +21.54 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.2443 | +21.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.018128 | +19.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.073979 | +18.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12329 | +18.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1236 scans ; 529273 observations ; 570 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
