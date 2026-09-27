# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T19:56:47.780406+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T19:56:18.045816+00:00 | âge ticker : 145.8 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.30876 € | IGNITION | score 85.75/100 | entrée 7.00/10
  Entrée 0.30877 € ; stop 0.29692 € ; TP1 0.33246 € ; TP2 0.34431 € ; montant 250.00 € ; risque théorique 11.31 € ; R/R net 1.54.
  Chase risk : 4.735/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XDC-EUR : 0.028524 € ; score 92.86/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.108665 € ; score 90.37/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11467 € ; score 89.83/100 ; SURVEILLE ; WICK_SETUP
- DATAIP-EUR : 0.2056 € ; score 89.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : 0.44286 € ; score 88.23/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 162.194 | +50.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28569 | +46.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.96568 | +30.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016297 | +28.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006483 | +27.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00737 | +23.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.013593 | +18.70 % | DETECTED_EARLY | NONE | NONE |
| GRT-EUR | 0.028515 | +17.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006914 | +16.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.23433 | +15.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1642 scans ; 702502 observations ; 1164 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
