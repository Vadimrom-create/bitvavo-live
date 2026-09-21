# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T12:53:24.606439+00:00
État : OK | marchés EUR : 426 | V4 : 393 | données valides : 426
Récupération : 2026-09-21T12:52:52.545743+00:00 | âge ticker : 153.3 s | durée : 154.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : 54.412 € | IGNITION | score 87.87/100 | entrée 7.65/10
  Entrée 54.414 € ; stop 52.069 € ; TP1 59.104 € ; TP2 61.449 € ; montant 240.27 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 6.256/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TIA-EUR : 0.38278 € ; score 89.44/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : 0.60401 € ; score 86.51/100 ; SURVEILLE ; WICK_SETUP
- TURBO-EUR : 0.000892 € ; score 85.12/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ETC-EUR : 7.676 € ; score 85.04/100 ; SURVEILLE ; seuil achat non atteint
- PIXEL-EUR : 0.0047144 € ; score 83.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055867 | +69.21 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.05163 | +66.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010458 | +50.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.031666 | +32.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.057292 | +31.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.05382 | +29.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23426 | +28.06 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.095691 | +26.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 0.90622 | +26.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARKM-EUR | 0.11612 | +24.34 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1077 scans ; 461539 observations ; 364 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
