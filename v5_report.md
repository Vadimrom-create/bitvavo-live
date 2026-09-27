# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T01:38:33.192894+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T01:38:03.678320+00:00 | âge ticker : 146.0 s | durée : 146.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : 0.011873 € | IGNITION | score 89.44/100 | entrée 6.80/10
  Entrée 0.01186 € ; stop 0.011402 € ; TP1 0.012776 € ; TP2 0.013234 € ; montant 250.00 € ; risque théorique 11.37 € ; R/R net 1.54.
  Chase risk : 6.437/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DATAIP-EUR : 0.2042 € ; score 92.06/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.83984 € ; score 91.27/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.11978 € ; score 89.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.99092 € ; score 86.15/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.23771 € ; score 86.13/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 147.625 | +67.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006734 | +51.16 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017622 | +35.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.060768 | +20.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.006163 | +18.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.20904 | +17.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.6773 | +17.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRC-EUR | 0.001275 | +16.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.006404 | +15.93 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| KMNO-EUR | 0.042066 | +15.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1578 scans ; 675174 observations ; 1059 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
