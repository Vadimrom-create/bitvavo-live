# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T01:30:16.881557+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-28T01:29:44.915062+00:00 | âge ticker : 147.9 s | durée : 148.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.12305 € | IGNITION | score 90.92/100 | entrée 6.80/10
  Entrée 0.12314 € ; stop 0.1186 € ; TP1 0.13222 € ; TP2 0.13676 € ; montant 250.00 € ; risque théorique 10.93 € ; R/R net 1.52.
  Chase risk : 2.955/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- EGLD-EUR : 4.0931 € ; score 92.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BABY-EUR : 0.012237 € ; score 92.26/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ELSA-EUR : 0.055872 € ; score 91.92/100 ; SURVEILLE ; SPREAD_RISK
- HBAR-EUR : 0.085459 € ; score 89.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.2808e-06 € ; score 87.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 230.27 | +40.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.28015 | +32.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INX-EUR | 0.006591 | +27.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030554 | +27.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.035 | +25.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.074758 | +18.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.017214 | +17.77 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PUMP-EUR | 0.0045337 | +17.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16704 | +15.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRUST-EUR | 0.06111 | +14.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1662 scans ; 711042 observations ; 1213 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
