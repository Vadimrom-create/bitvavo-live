# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T08:06:47.664088+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T08:06:14.159779+00:00 | âge ticker : 150.0 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.101692 € | IGNITION | score 93.06/100 | entrée 7.70/10
  Entrée 0.10167 € ; stop 0.09733 € ; TP1 0.110349 € ; TP2 0.114689 € ; montant 242.24 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.708/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PYTH-EUR : 0.065705 € ; score 91.64/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DIA-EUR : 0.14232 € ; score 91.31/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- CFG-EUR : 0.140658 € ; score 90.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.011046 € ; score 88.15/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALICE-EUR : 0.14451 € ; score 87.03/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0015543 | +99.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020037 | +73.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.068317 | +38.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.25337 | +34.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.06181 | +28.64 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENA-EUR | 0.23899 | +22.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.77176 | +20.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.038651 | +17.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.12005 | +17.14 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PUMP-EUR | 0.003998 | +16.29 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1515 scans ; 648273 observations ; 958 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
