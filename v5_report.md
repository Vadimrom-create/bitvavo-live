# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T14:19:28.756087+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T14:19:00.459843+00:00 | âge ticker : 150.9 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- MEGA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.085013 € | IGNITION | score 92.61/100 | entrée 8.00/10
  Entrée 0.085006 € ; stop 0.081278 € ; TP1 0.092461 € ; TP2 0.096189 € ; montant 236.68 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.819/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.221 € | IGNITION | score 83.41/100 | entrée 7.70/10
  Entrée 0.22116 € ; stop 0.21228 € ; TP1 0.23892 € ; TP2 0.2478 € ; montant 250.00 € ; risque théorique 11.75 € ; R/R net 1.55.
  Chase risk : 3.748/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SSV-EUR : 2.8603 € ; score 90.65/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.3735 € ; score 90.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.058608 € ; score 89.23/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.001682 € ; score 88.44/100 ; SURVEILLE ; SPREAD_RISK
- ARK-EUR : 0.13637 € ; score 86.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016543 | +90.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013362 | +70.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.074654 | +32.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.083289 | +32.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.052164 | +26.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 281.36 | +20.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.33999 | +20.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.000492 | +17.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.27361 | +16.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.3765 | +15.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1191 scans ; 510103 observations ; 508 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
