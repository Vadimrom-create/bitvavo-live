# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:37:33.652940+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:37:00.005457+00:00 | âge ticker : 148.3 s | durée : 148.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- POL-EUR : 0.098348 € ; score 89.87/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.13734 € ; score 86.20/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.029598 € ; score 84.03/100 ; SURVEILLE ; seuil achat non atteint
- ALIGN-EUR : 0.005949 € ; score 84.02/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- VET-EUR : 0.0080419 € ; score 83.75/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014656 | +89.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016 | +86.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.128548 | +59.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052668 | +52.87 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31523 | +40.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008865 | +38.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043574 | +34.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010871 | +33.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.026199 | +24.50 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SYN-EUR | 0.230789 | +22.29 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1127 scans ; 482839 observations ; 407 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
