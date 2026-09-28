# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T13:32:33.821183+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 427
Récupération : 2026-09-28T13:31:59.609217+00:00 | âge ticker : 158.9 s | durée : 160.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.6037 € | IGNITION | score 81.99/100 | entrée 6.90/10
  Entrée 4.6035 € ; stop 4.4282 € ; TP1 4.9541 € ; TP2 5.1294 € ; montant 250.00 € ; risque théorique 11.24 € ; R/R net 1.53.
  Chase risk : 3.751/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LINK-EUR : 12.9215 € | IGNITION | score 81.52/100 | entrée 6.55/10
  Entrée 12.9419 € ; stop 12.2215 € ; TP1 14.3827 € ; TP2 15.1031 € ; montant 192.09 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 6.879/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.19726 € | IGNITION | score 79.41/100 | entrée 6.25/10
  Entrée 0.19726 € ; stop 0.18478 € ; TP1 0.22221 € ; TP2 0.23469 € ; montant 10.90 € ; risque théorique 0.76 € ; R/R net 1.70.
  Chase risk : 6.44/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.012669 € ; score 90.57/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11102 € ; score 88.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- RENDER-EUR : 1.734 € ; score 86.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RUNE-EUR : 0.65345 € ; score 86.72/100 ; SURVEILLE ; WICK_SETUP
- VVV-EUR : 25.0426 € ; score 85.79/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 214.377 | +48.31 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.10462 | +26.26 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 9.9119 | +16.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0046301 | +15.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.028294 | +15.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.115202 | +12.16 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.025814 | +11.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.070844 | +9.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016037 | +9.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.282 | +8.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1697 scans ; 725989 observations ; 1245 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
