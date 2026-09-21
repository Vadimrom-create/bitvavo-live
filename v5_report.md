# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:36:39.996837+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T21:35:37.729193+00:00 | âge ticker : 184.0 s | durée : 188.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.29972 € | IGNITION | score 81.54/100 | entrée 6.95/10
  Entrée 0.29932 € ; stop 0.28856 € ; TP1 0.32083 € ; TP2 0.33159 € ; montant 250.00 € ; risque théorique 10.71 € ; R/R net 1.51.
  Chase risk : 3.321/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GRT-EUR : 0.020365 € ; score 92.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BCH-EUR : 233.89 € ; score 86.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- YFI-EUR : 2010.1 € ; score 83.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ENS-EUR : 5.9462 € ; score 83.19/100 ; SURVEILLE ; seuil achat non atteint
- PORTAL-EUR : 0.017193 € ; score 82.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017049 | +117.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016857 | +96.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052837 | +53.36 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31328 | +39.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.110306 | +37.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.043771 | +36.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWELL-EUR | 0.0008472 | +30.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010578 | +30.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.39058 | +25.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.257323 | +24.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1119 scans ; 479431 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
