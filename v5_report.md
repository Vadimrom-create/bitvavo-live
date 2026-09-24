# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T08:15:24.883378+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T08:15:00.427446+00:00 | âge ticker : 141.8 s | durée : 142.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 8.4253 € | IGNITION | score 93.14/100 | entrée 7.40/10
  Entrée 8.4236 € ; stop 8.0623 € ; TP1 9.1462 € ; TP2 9.5075 € ; montant 241.25 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.381/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAO-EUR : 255.33 € ; score 91.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SHELL-EUR : 0.024263 € ; score 90.66/100 ; SURVEILLE ; LOW_LIQUIDITY
- DEEP-EUR : 0.016764 € ; score 90.62/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.044399 € ; score 90.56/100 ; SURVEILLE ; seuil achat non atteint
- LPT-EUR : 1.4454 € ; score 90.05/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0023113 | +51.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.1257 | +41.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38472 | +39.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.85353 | +17.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019488 | +13.00 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CELR-EUR | 0.0028506 | +10.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28859 | +9.91 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| LTC-EUR | 60.648 | +8.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.385 | +8.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.01815 | +7.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1340 scans ; 573577 observations ; 695 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
