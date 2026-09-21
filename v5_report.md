# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:49:49.816736+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T21:49:16.360813+00:00 | âge ticker : 155.7 s | durée : 156.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.6174 € | IGNITION | score 78.69/100 | entrée 8.30/10
  Entrée 1.6151 € ; stop 1.5545 € ; TP1 1.7363 € ; TP2 1.7969 € ; montant 250.00 € ; risque théorique 11.10 € ; R/R net 1.53.
  Chase risk : 4.191/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PORTAL-EUR : 0.017134 € ; score 90.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- THE-EUR : 0.07074 € ; score 88.53/100 ; SURVEILLE ; seuil achat non atteint
- KAITO-EUR : 0.30026 € ; score 87.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOLV-EUR : 0.0036172 € ; score 87.37/100 ; SURVEILLE ; seuil achat non atteint
- DOT-EUR : 1.0392 € ; score 86.63/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015691 | +100.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016273 | +89.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052368 | +52.00 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31492 | +40.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043776 | +35.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.00088 | +35.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.10799 | +34.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010695 | +32.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.026133 | +24.32 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| GRASS-EUR | 0.38828 | +23.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1121 scans ; 480283 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
