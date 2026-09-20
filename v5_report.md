# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T20:07:40.960928+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-20T20:06:38.806592+00:00 | âge ticker : 181.2 s | durée : 182.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.37418 € | IGNITION | score 85.61/100 | entrée 7.00/10
  Entrée 0.37434 € ; stop 0.36016 € ; TP1 0.4027 € ; TP2 0.41688 € ; montant 250.00 € ; risque théorique 11.19 € ; R/R net 1.53.
  Chase risk : 2.159/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PUMP-EUR : 0.0037591 € | IGNITION | score 80.48/100 | entrée 6.10/10
  Entrée 0.0037598 € ; stop 0.0035891 € ; TP1 0.0041012 € ; TP2 0.0042719 € ; montant 229.70 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.406/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAKE-EUR : 2.2156 € ; score 89.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AAVE-EUR : 119.55 € ; score 88.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.1357 € ; score 87.18/100 ; SURVEILLE ; seuil achat non atteint
- PENGU-EUR : 0.0068674 € ; score 86.86/100 ; SURVEILLE ; STABILITY_HOLD
- VET-EUR : 0.0073543 € ; score 85.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.034342 | +58.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.28277 | +53.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007862 | +27.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.035081 | +24.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0030776 | +20.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6278 | +18.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.042899 | +17.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.049 | +17.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.7464 | +16.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027912 | +16.30 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1013 scans ; 434275 observations ; 253 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
