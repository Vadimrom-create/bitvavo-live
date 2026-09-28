# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T00:00:14.448688+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-27T23:59:41.761569+00:00 | âge ticker : 155.6 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KMNO-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TIA-EUR : 0.44782 € | IGNITION | score 86.51/100 | entrée 7.00/10
  Entrée 0.44809 € ; stop 0.43026 € ; TP1 0.48375 € ; TP2 0.50158 € ; montant 250.00 € ; risque théorique 11.66 € ; R/R net 1.55.
  Chase risk : 2.424/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- EIGEN-EUR : 0.2437 € | IGNITION | score 84.74/100 | entrée 6.70/10
  Entrée 0.2427 € ; stop 0.23353 € ; TP1 0.26104 € ; TP2 0.27021 € ; montant 250.00 € ; risque théorique 11.16 € ; R/R net 1.53.
  Chase risk : 2.285/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CFG-EUR : 0.146467 € ; score 93.77/100 ; SURVEILLE ; seuil achat non atteint
- APE-EUR : 0.14468 € ; score 93.64/100 ; SURVEILLE ; WICK_SETUP
- SENT-EUR : 0.019705 € ; score 93.09/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.2058 € ; score 93.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.74081 € ; score 92.48/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 249.099 | +86.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.29115 | +44.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006787 | +30.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.031482 | +29.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.95769 | +21.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.01379 | +19.57 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0045295 | +17.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16795 | +16.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020726 | +14.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0047083 | +14.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1658 scans ; 709334 observations ; 1207 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
