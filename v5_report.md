# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T05:18:27.471596+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T05:17:56.548813+00:00 | âge ticker : 156.9 s | durée : 158.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0085928 € | IGNITION | score 87.41/100 | entrée 7.20/10
  Entrée 0.0086179 € ; stop 0.0082624 € ; TP1 0.0093289 € ; TP2 0.0096844 € ; montant 249.44 € ; risque théorique 12.00 € ; R/R net 1.56.
  Chase risk : 3.005/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- UNI-EUR : 8.4864 € ; score 91.32/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- IO-EUR : 0.14609 € ; score 87.14/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AZTEC-EUR : 0.014618 € ; score 86.94/100 ; SURVEILLE ; seuil achat non atteint
- XTZ-EUR : 0.285 € ; score 86.29/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ALT-EUR : 0.0070065 € ; score 85.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017033 | +119.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.074292 | +69.32 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.23176 | +31.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78742 | +26.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24156 | +24.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065145 | +18.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.033044 | +16.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.013234 | +16.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WAXP-EUR | 0.0060655 | +16.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JTO-EUR | 0.50529 | +16.17 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1505 scans ; 644003 observations ; 947 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
