# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T10:01:51.969392+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-26T10:01:22.257462+00:00 | âge ticker : 153.7 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XPL-EUR : 0.103704 € | IGNITION | score 81.24/100 | entrée 7.40/10
  Entrée 0.103588 € ; stop 0.099061 € ; TP1 0.112642 € ; TP2 0.117169 € ; montant 237.39 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.848/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ALT-EUR : 0.0071931 € ; score 90.39/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- C-EUR : 0.078134 € ; score 88.78/100 ; SURVEILLE ; WICK_SETUP
- SLP-EUR : 0.00063553 € ; score 88.72/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- API3-EUR : 0.2527 € ; score 88.49/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0019401 € ; score 87.68/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020814 | +163.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020432 | +76.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.066645 | +37.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.068529 | +30.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.23878 | +25.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24454 | +25.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7964 | +17.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TNSR-EUR | 0.0395 | +16.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.098063 | +16.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.5304 | +14.72 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1522 scans ; 651262 observations ; 969 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
