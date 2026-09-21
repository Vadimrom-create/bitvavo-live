# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:04:36.842945+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T21:04:08.162749+00:00 | âge ticker : 145.1 s | durée : 145.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : LOW_LIQUIDITY, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.3947 € | IGNITION | score 92.73/100 | entrée 8.40/10
  Entrée 0.3944 € ; stop 0.38027 € ; TP1 0.42265 € ; TP2 0.43678 € ; montant 250.00 € ; risque théorique 10.68 € ; R/R net 1.51.
  Chase risk : 2.988/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- STX-EUR : 0.30284 € | IGNITION | score 85.38/100 | entrée 7.10/10
  Entrée 0.3016 € ; stop 0.28564 € ; TP1 0.33351 € ; TP2 0.34947 € ; montant 200.90 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 6.592/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GOAT-EUR : 0.016122 € ; score 89.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XRP-EUR : 1.33162 € ; score 86.86/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TRUMP-EUR : 1.9092 € ; score 85.09/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 103.871 € ; score 84.97/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OPEN-EUR : 0.12464 € ; score 84.58/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017721 | +126.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017601 | +108.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053224 | +54.48 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31741 | +41.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.110763 | +39.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.04372 | +36.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010608 | +34.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.259898 | +25.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.232633 | +25.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.2617e-06 | +23.93 % | DETECTED_EARLY | NONE | NONE |

Historique : 1116 scans ; 478153 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
