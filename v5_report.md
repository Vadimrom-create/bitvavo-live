# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T21:24:11.534106+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T21:23:14.904796+00:00 | âge ticker : 173.5 s | durée : 174.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : 64.737 € | IGNITION | score 90.30/100 | entrée 7.60/10
  Entrée 64.811 € ; stop 62.351 € ; TP1 69.731 € ; TP2 72.191 € ; montant 250.00 € ; risque théorique 11.21 € ; R/R net 1.53.
  Chase risk : 2.207/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZORA-EUR : 0.007783 € ; score 91.16/100 ; SURVEILLE ; seuil achat non atteint
- TRUST-EUR : 0.054257 € ; score 89.93/100 ; SURVEILLE ; seuil achat non atteint
- FLOKI-EUR : 2.605e-05 € ; score 89.82/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- LUNA-EUR : 4.8904e-05 € ; score 86.60/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MIRA-EUR : 0.047711 € ; score 85.28/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019922 | +35.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020371 | +31.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 300.74 | +28.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051758 | +22.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0089754 | +18.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068951 | +16.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.075523 | +16.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12073 | +16.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.297336 | +16.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.1914 | +15.31 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1217 scans ; 521179 observations ; 539 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
