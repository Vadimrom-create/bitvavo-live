# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T02:02:56.983995+00:00
État : OK | marchés EUR : 429 | V4 : 391 | données valides : 429
Récupération : 2026-09-30T02:02:25.283876+00:00 | âge ticker : 147.2 s | durée : 147.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.34535 € | IGNITION | score 92.49/100 | entrée 7.50/10
  Entrée 0.34417 € ; stop 0.32852 € ; TP1 0.37546 € ; TP2 0.39111 € ; montant 229.39 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.704/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ROSE-EUR : 0.008096 € ; score 89.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.038575 € ; score 85.92/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0027996 € ; score 84.47/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 5.1098e-06 € ; score 83.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ILV-EUR : 3.4877 € ; score 82.82/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 251.258 | +36.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.34202 | +33.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.1011 | +32.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016217 | +31.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65141 | +28.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEW-EUR | 0.00050456 | +24.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051772 | +23.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.090206 | +18.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.06358 | +18.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5536 | +17.89 % | DETECTED_EARLY | NONE | NONE |

Historique : 1809 scans ; 773971 observations ; 1352 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
