# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:30:55.548353+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:30:24.170708+00:00 | âge ticker : 146.2 s | durée : 146.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MIOTA-EUR : 0.042027 € ; score 88.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AI-EUR : 0.018481 € ; score 87.34/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.098186 € ; score 87.04/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.13734 € ; score 85.97/100 ; SURVEILLE ; seuil achat non atteint
- JUP-EUR : 0.25834 € ; score 83.84/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014606 | +88.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.014663 | +70.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.124757 | +55.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052292 | +51.78 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31564 | +40.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.000873 | +36.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010909 | +35.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.04316 | +33.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.026244 | +24.72 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SYN-EUR | 0.229812 | +22.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1126 scans ; 482413 observations ; 407 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
