# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T13:34:16.047300+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-23T13:33:39.998760+00:00 | âge ticker : 160.7 s | durée : 161.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- USELESS-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VVV-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TAIKO-EUR : 0.08096 € ; score 88.58/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0018336 € ; score 83.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- ETC-EUR : 8.2735 € ; score 83.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.698 € ; score 82.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MIOTA-EUR : 0.042536 € ; score 82.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.035894 | +50.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.34159 | +34.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.305852 | +34.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020848 | +25.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.042261 | +24.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16107 | +20.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017014 | +17.93 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.2741 | +17.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.024014 | +15.69 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CHR-EUR | 0.018126 | +14.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1272 scans ; 544609 observations ; 650 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
