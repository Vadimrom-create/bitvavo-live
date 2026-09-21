# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:44:38.506281+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:44:05.128393+00:00 | âge ticker : 149.9 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- POL-EUR : 0.09832 € ; score 90.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.13723 € ; score 86.49/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.006704 € ; score 86.48/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- FIL-EUR : 0.86479 € ; score 86.19/100 ; SURVEILLE ; seuil achat non atteint
- ALIGN-EUR : 0.005936 € ; score 84.98/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0165 | +92.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.00147 | +89.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.1238 | +55.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052339 | +51.91 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31353 | +39.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008741 | +36.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043232 | +34.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010832 | +33.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.02603 | +23.59 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| GRASS-EUR | 0.38 | +21.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1128 scans ; 483265 observations ; 407 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
