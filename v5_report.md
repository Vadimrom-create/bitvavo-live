# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T00:58:47.201391+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T00:58:18.252923+00:00 | âge ticker : 149.6 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.92003 € | IGNITION | score 92.61/100 | entrée 8.30/10
  Entrée 0.92176 € ; stop 0.87741 € ; TP1 1.01046 € ; TP2 1.05481 € ; montant 218.40 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 2.171/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GMT-EUR : 0.007696 € ; score 92.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.082089 € ; score 92.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.19418 € ; score 91.03/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.2197 € ; score 91.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : 1.35873 € ; score 89.74/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.059984 | +43.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 79.637 | +28.80 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.46113 | +28.00 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.100456 | +27.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.1748 | +26.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.60536 | +25.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.02167 | +22.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.008327 | +19.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DYM-EUR | 0.018669 | +18.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.036222 | +18.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1404 scans ; 600876 observations ; 789 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
