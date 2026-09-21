# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T13:09:20.489356+00:00
État : OK | marchés EUR : 426 | V4 : 393 | données valides : 426
Récupération : 2026-09-21T13:08:21.491461+00:00 | âge ticker : 178.5 s | durée : 179.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PENDLE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : 0.100621 € | IGNITION | score 85.53/100 | entrée 7.35/10
  Entrée 0.100707 € ; stop 0.097135 € ; TP1 0.107851 € ; TP2 0.111423 € ; montant 250.00 € ; risque théorique 10.59 € ; R/R net 1.50.
  Chase risk : 4.62/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TIA-EUR : 0.3869 € | IGNITION | score 83.79/100 | entrée 6.70/10
  Entrée 0.38882 € ; stop 0.37437 € ; TP1 0.41772 € ; TP2 0.43217 € ; montant 250.00 € ; risque théorique 11.01 € ; R/R net 1.52.
  Chase risk : 4.615/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.55281 € | IGNITION | score 82.59/100 | entrée 7.00/10
  Entrée 1.5546 € ; stop 1.48838 € ; TP1 1.68703 € ; TP2 1.75325 € ; montant 48.64 € ; risque théorique 2.41 € ; R/R net 1.58.
  Chase risk : 3.105/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RSR-EUR : 0.0014624 € ; score 92.29/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0052904 € ; score 85.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AERO-EUR : 0.609 € ; score 84.38/100 ; SURVEILLE ; WICK_SETUP
- ALIGN-EUR : 0.005892 € ; score 84.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MERL-EUR : 0.024005 € ; score 83.22/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055689 | +68.67 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.051126 | +64.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010453 | +48.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.032034 | +33.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.10094 | +32.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.057225 | +32.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.053325 | +29.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.91763 | +28.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.23178 | +26.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.5062 | +25.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1078 scans ; 461965 observations ; 372 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
