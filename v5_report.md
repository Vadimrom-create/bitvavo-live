# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T11:23:35.238178+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T11:23:06.945638+00:00 | âge ticker : 140.6 s | durée : 141.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZORA-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.0019746 € | IGNITION | score 86.43/100 | entrée 7.05/10
  Entrée 0.0019747 € ; stop 0.0018804 € ; TP1 0.0021632 € ; TP2 0.0022575 € ; montant 219.83 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.688/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- W-EUR : 0.011326 € | IGNITION | score 84.17/100 | entrée 7.00/10
  Entrée 0.01137 € ; stop 0.010926 € ; TP1 0.012258 € ; TP2 0.012702 € ; montant 250.00 € ; risque théorique 11.48 € ; R/R net 1.54.
  Chase risk : 3.262/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- OP-EUR : 0.12952 € | IGNITION | score 83.64/100 | entrée 7.60/10
  Entrée 0.12967 € ; stop 0.12407 € ; TP1 0.14087 € ; TP2 0.14647 € ; montant 10.43 € ; risque théorique 0.52 € ; R/R net 1.58.
  Chase risk : 3.499/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 12.575 € ; score 94.22/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.103957 € ; score 93.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.8106 € ; score 92.90/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZORA-EUR : 0.007991 € ; score 91.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SAND-EUR : 0.040389 € ; score 91.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00201 | +151.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.021838 | +84.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.064893 | +33.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.070222 | +27.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.8307 | +21.02 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ENA-EUR | 0.25054 | +19.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.79353 | +15.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24341 | +15.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TNSR-EUR | 0.038694 | +13.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.03987 | +12.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1527 scans ; 653397 observations ; 979 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
