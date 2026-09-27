# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T08:59:20.717316+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T08:58:52.734106+00:00 | âge ticker : 147.4 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.52712 € | IGNITION | score 90.48/100 | entrée 7.10/10
  Entrée 1.52828 € ; stop 1.45848 € ; TP1 1.66788 € ; TP2 1.73768 € ; montant 228.52 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 6.984/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CRO-EUR : 0.059817 € ; score 92.79/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SHIB-EUR : 5.2668e-06 € ; score 88.93/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PROM-EUR : 5.4824 € ; score 88.69/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- EIGEN-EUR : 0.24811 € ; score 88.66/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ESP-EUR : 0.09173 € ; score 88.36/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 158.25 | +75.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.009149 | +56.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.27426 | +46.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006033 | +32.83 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006857 | +24.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006327 | +24.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.116564 | +20.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.01324 | +18.35 % | DETECTED_EARLY | NONE | NONE |
| XVG-EUR | 0.0032169 | +18.04 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TRIA-EUR | 0.004225 | +16.81 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1603 scans ; 685849 observations ; 1102 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
