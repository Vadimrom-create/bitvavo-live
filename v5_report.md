# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T16:25:56.703567+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-26T16:25:29.026263+00:00 | âge ticker : 149.3 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.1199 € | IGNITION | score 86.82/100 | entrée 7.20/10
  Entrée 1.1207 € ; stop 1.0699 € ; TP1 1.2223 € ; TP2 1.2731 € ; montant 230.02 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.478/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ICP-EUR : 2.9184 € | IGNITION | score 83.45/100 | entrée 7.55/10
  Entrée 2.924 € ; stop 2.8103 € ; TP1 3.1514 € ; TP2 3.2651 € ; montant 250.00 € ; risque théorique 11.44 € ; R/R net 1.54.
  Chase risk : 3.755/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.083325 € ; score 93.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.19303 € ; score 93.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALLO-EUR : 0.270928 € ; score 90.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MAVIA-EUR : 0.031136 € ; score 90.53/100 ; SURVEILLE ; WICK_SETUP
- POL-EUR : 0.104317 € ; score 90.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017578 | +117.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.1154 | +33.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.000585 | +31.20 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.01926 | +28.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 104.527 | +23.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.20153 | +20.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.6703 | +19.32 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| 2Z-EUR | 0.060107 | +18.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.0439 | +18.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.47323 | +17.65 % | DETECTED_EARLY | NONE | NONE |

Historique : 1545 scans ; 661083 observations ; 1013 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
