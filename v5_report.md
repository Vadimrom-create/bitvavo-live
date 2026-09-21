# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T11:39:16.637783+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 426
Récupération : 2026-09-21T11:38:44.867811+00:00 | âge ticker : 154.6 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : 0.39273 € | IGNITION | score 92.18/100 | entrée 8.15/10
  Entrée 0.39263 € ; stop 0.376 € ; TP1 0.42588 € ; TP2 0.44251 € ; montant 243.87 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 5.4/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MERL-EUR : 0.024021 € ; score 94.79/100 ; SURVEILLE ; WICK_SETUP
- GRASS-EUR : 0.32841 € ; score 92.00/100 ; SURVEILLE ; WICK_SETUP
- MANTA-EUR : 0.062488 € ; score 89.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FIL-EUR : 0.86261 € ; score 87.86/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.097845 € ; score 86.96/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056722 | +70.42 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.050813 | +62.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010231 | +48.49 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.24263 | +32.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.031236 | +30.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.05625 | +30.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.053195 | +28.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.89374 | +25.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031605 | +23.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CETUS-EUR | 0.025252 | +22.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1072 scans ; 459409 observations ; 354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
