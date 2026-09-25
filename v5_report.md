# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T00:42:34.919755+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T00:41:37.037433+00:00 | âge ticker : 177.0 s | durée : 177.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.19501 € | IGNITION | score 93.65/100 | entrée 7.90/10
  Entrée 0.19497 € ; stop 0.18647 € ; TP1 0.21197 € ; TP2 0.22047 € ; montant 237.89 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.776/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DATAIP-EUR : 0.1992 € | IGNITION | score 76.20/100 | entrée 7.15/10
  Entrée 0.1993 € ; stop 0.1891 € ; TP1 0.2197 € ; TP2 0.2299 € ; montant 206.90 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 1.181/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ALGO-EUR : 0.099824 € ; score 93.18/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.6476 € ; score 92.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.21974 € ; score 90.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.082274 € ; score 89.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.03535 € ; score 88.54/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.068232 | +63.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.18122 | +30.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.46194 | +28.02 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 78.989 | +27.75 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.100111 | +26.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.60915 | +24.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XAI-EUR | 0.0083537 | +20.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021892 | +19.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.03628 | +19.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20149 | +18.52 % | DETECTED_EARLY | NONE | NONE |

Historique : 1403 scans ; 600449 observations ; 789 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
