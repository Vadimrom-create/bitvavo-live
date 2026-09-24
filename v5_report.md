# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T11:16:53.102188+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-24T11:16:19.533863+00:00 | âge ticker : 150.5 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.5771 € | IGNITION | score 87.58/100 | entrée 7.05/10
  Entrée 1.5746 € ; stop 1.5131 € ; TP1 1.6976 € ; TP2 1.7591 € ; montant 250.00 € ; risque théorique 11.48 € ; R/R net 1.54.
  Chase risk : 2.431/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ETC-EUR : 8.4203 € | IGNITION | score 84.84/100 | entrée 6.70/10
  Entrée 8.4269 € ; stop 8.0269 € ; TP1 9.2269 € ; TP2 9.6269 € ; montant 220.99 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 3.9/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WAL-EUR : 0.028345 € ; score 91.04/100 ; SURVEILLE ; seuil achat non atteint
- CAT-EUR : 1.9979e-06 € ; score 86.97/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- QNT-EUR : 63.701 € ; score 86.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GOAT-EUR : 0.01679 € ; score 85.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DYDX-EUR : 0.11216 € ; score 84.49/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.00213 | +37.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.112118 | +32.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IMU-EUR | 0.0020492 | +20.56 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.34089 | +19.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21916 | +17.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.39501 | +12.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.2911 | +10.71 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CVC-EUR | 0.02729 | +9.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.15237 | +8.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BEAM-EUR | 0.0018174 | +6.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1350 scans ; 577837 observations ; 713 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
