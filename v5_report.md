# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T13:19:12.433902+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-22T13:18:45.045076+00:00 | âge ticker : 144.5 s | durée : 145.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZORA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0080483 € | IGNITION | score 81.71/100 | entrée 7.25/10
  Entrée 0.0080554 € ; stop 0.0077722 € ; TP1 0.0086218 € ; TP2 0.008905 € ; montant 250.00 € ; risque théorique 10.51 € ; R/R net 1.50.
  Chase risk : 3.182/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- THE-EUR : 0.07299 € ; score 92.06/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.097084 € ; score 90.59/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.18648 € ; score 90.29/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.087334 € ; score 89.56/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MEME-EUR : 0.00053476 € ; score 89.06/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.001477 | +87.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016209 | +83.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KERNEL-EUR | 0.052506 | +26.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.00053 | +23.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.28799 | +23.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.070595 | +22.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.38313 | +18.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.23236 | +18.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 277.1 | +18.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.073827 | +17.43 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1187 scans ; 508399 observations ; 506 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
